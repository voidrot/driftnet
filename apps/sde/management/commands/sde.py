import logging
import sys
import zipfile
from pathlib import Path
from typing import Any

import httpx
import inflect
import jsonlines
import textcase
from django.core.management.base import BaseCommand
from yaml import load

from apps.sde import app_settings
from apps.sde.management.commands._helpers import DO_NOT_CONVERT_TO_CAMEL_FILES
from apps.sde.management.commands._helpers import IGNORED_CONVERT_TO_SINGULAR
from apps.sde.management.commands._helpers import IGNORED_FILES
from apps.sde.models import *  # noqa: F403

p = inflect.engine()

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Perform SDE tasks'

    workspace_dir = Path(app_settings.SDE_WORKSPACE)

    def add_arguments(self, parser):
        parser.add_argument(
            '--force-download',
            action='store_true',
            help='Force fresh download and import of the SDE',
        )

        parser.add_argument(
            '--download-only',
            action='store_true',
            help='Only download the SDE and extract, skip further processing',
        )

        parser.add_argument(
            '--skip-download',
            action='store_true',
            help='Skip downloading the SDE, assume it is already present in the workspace',
        )

        parser.add_argument(
            '--check-version',
            action='store_true',
            help='Check for the latest SDE version and exit',
        )

    # Setup the SDE workspace
    def setup_workspace(self) -> None:
        logger.info('Setting up workspace for SDE tasks')
        self.workspace_dir.mkdir(parents=True, exist_ok=True)

    def get_changelog(self) -> None:
        logger.info('Fetching SDE changelog')
        changelog_url = app_settings.SDE_CHANGELOG_URL
        # Fetch the changelog

        response = httpx.get(changelog_url, timeout=30)
        response.raise_for_status()

        self.schema_changelog = load(response.text, Loader=Loader)['schemaChangelog']

    def download_sde_export(self) -> None:
        logger.info('Downloading SDE export')
        sde_url = app_settings.SDE_LATEST_SDE_EXPORT_URL
        local_zip_path = self.workspace_dir / app_settings.SDE_ZIPFILE_DOWNLOAD_NAME

        # Must follow redirects since we are using the latest shortcut
        response = httpx.get(sde_url, timeout=60, follow_redirects=True)
        response.raise_for_status()

        with open(local_zip_path, 'wb') as f:
            f.write(response.content)

        logger.info(f'SDE export downloaded to {local_zip_path}')

        # Extract the zip file
        with zipfile.ZipFile(local_zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.workspace_dir / 'extracted')

        logger.info(f'SDE export extracted to {self.workspace_dir / "extracted"}')

    def store_changelog(self, changelog: list[dict[str, Any]]) -> None:
        existing_changelog = Changelog.objects.all()

        for change in changelog:
            if not existing_changelog.filter(
                build_number=change['afterBuildNumber']
            ).exists():
                Changelog.objects.create(
                    build_number=change['afterBuildNumber'],
                    change_date=change.get('date', ''),
                    file_changes=change.get('files', {}),
                    field_changes=change.get('fields', {}),
                )
                logger.info(f'New changelog entry added: {change["afterBuildNumber"]}')

    def check_schema_changelog_version(self) -> None:
        latest_entry = Changelog.objects.order_by('-build_number').first()
        latest_build_number = latest_entry.build_number if latest_entry else None
        latest_schema_build_number = self.schema_changelog[0]['afterBuildNumber']

        if latest_build_number == latest_schema_build_number:
            logger.info('SDE is up to date.')
            sys.exit(0)
        else:
            logger.warning(
                f'SDE is outdated. Latest in DB: {latest_build_number}, Latest available: {latest_schema_build_number}'
            )
            sys.exit(1)

    def get_last_schema_changelog_entry(self) -> int | None:
        last_entry = Changelog.objects.order_by('-build_number').first()
        if last_entry:
            return last_entry.build_number
        return 0

    def get_latest_remote_schema_changelog_entry(self) -> int:
        res = httpx.get(app_settings.SDE_LATEST_CHANGELOG_VERSION_URL, timeout=30)
        res.raise_for_status()
        return res.json().get('buildNumber', 0)

    def convert_to_singular_noun(self, name):
        """Convert a string to singular noun."""
        word = p.singular_noun(name)
        if not word:
            logger.warning(f'Failed to convert {name} to singular noun.')
            return name
        return word

    def get_data_files_list(self) -> None:
        self.data_files = [
            f
            for f in (self.workspace_dir / 'extracted').glob('*.jsonl')
            if f.is_file() and f.name not in IGNORED_FILES
        ]
        logger.debug(f'Found {len(self.data_files)} data files in extracted directory.')

    def convert_field_name_to_camel(self, field_name: str, file_name: str) -> str:
        if file_name in DO_NOT_CONVERT_TO_CAMEL_FILES:
            return field_name
        if field_name.endswith('_id'):
            return textcase.camel(field_name[:-3]) + 'ID'
        if field_name.endswith('_ids'):
            return textcase.camel(field_name[:-4]) + 'IDs'
        if field_name.endswith('ccpdevs'):
            return textcase.camel(field_name[:-7]) + 'CCPDevs'
        if field_name.endswith('_ui'):
            return textcase.camel(field_name[:-3]) + 'UI'
        return textcase.camel(field_name)

    def convert_file_name_to_model_name(self, file_name: Path) -> str:
        if file_name.name in IGNORED_CONVERT_TO_SINGULAR:
            return textcase.pascal(file_name.stem)  # Remove .jsonl
        return self.convert_to_singular_noun(
            textcase.pascal(file_name.stem)
        )  # Remove .jsonl

    def load_data_from_file(self, file: Path) -> None:
        # Get model name from file name (without extension)
        model_name = self.convert_file_name_to_model_name(file)
        model = globals().get(model_name)
        if model is None:
            logger.warning(f"Model '{model_name}' not found for file '{file.name}'")
            return

        # Get model fields (excluding auto fields and many-to-many)
        model_fields = [
            f.name
            for f in model._meta.get_fields()
            if f.concrete and not f.many_to_many
        ]

        # Prepare data for bulk_create
        data = []
        with jsonlines.open(file) as reader:
            for obj in reader:
                item_kwargs = {}
                for field in model_fields:
                    if field == 'id':
                        # Always map 'id' from '_key' in the data
                        item_kwargs['id'] = obj.get('_key')
                    else:
                        # Custom camelKey logic for _id/_ids suffixes
                        camel_key = self.convert_field_name_to_camel(field, file.name)
                        item_kwargs[field] = obj.get(camel_key)
                data.append(model(**item_kwargs))

        if data:
            # Use bulk_create with update_conflicts if possible
            try:
                update_fields = (
                    [f for f in model_fields if f != 'id']
                    if 'id' in model_fields
                    else model_fields
                )
                model.objects.bulk_create(
                    data,
                    update_conflicts=True,
                    update_fields=update_fields,
                    unique_fields=['id'] if 'id' in model_fields else None,
                )
                logger.info(f'Loaded {len(data)} records into {model_name}')
            except Exception as e:
                logger.exception(f'Error bulk creating {model_name}: {e}')
        else:
            logger.info(f'No data found in file {file.name}')

    def load_data_to_models(self) -> None:
        for file in self.data_files:
            sys.stdout.write(self.style.NOTICE(f'Processing file: {file.name}\n'))
            self.load_data_from_file(file)

    def handle(self, *args, **options) -> None:
        self.get_changelog()
        self.store_changelog(self.schema_changelog)

        if options['check_version']:
            self.check_schema_changelog_version()
            return

        self.setup_workspace()

        if not options['skip_download']:
            self.download_sde_export()

        if options['download_only']:
            logger.info('Download Only flag set, SDE is now downloaded and extracted.')
            return

        self.get_data_files_list()

        self.load_data_to_models()
