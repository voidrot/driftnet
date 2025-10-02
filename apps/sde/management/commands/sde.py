import os
from pprint import pprint
import sys
import httpx
import jsonlines
import logging
from django.conf import settings
from django.core.management.base import BaseCommand
from apps.sde import app_settings
import argparse
import hashlib
import json
import logging
import shutil
import subprocess
import zipfile
from pathlib import Path
from pathlib import Path as _Path
from typing import Any
from warnings import deprecated
from yaml import load, dump

from apps.sde.models.changelog import Changelog
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

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
            if not existing_changelog.filter(build_number=change['afterBuildNumber']).exists():
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
            logger.warning(f'SDE is outdated. Latest in DB: {latest_build_number}, Latest available: {latest_schema_build_number}')
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

    def determine_required_updates(self) -> list[dict[str, Any]]:
        pass



    def handle(self, *args, **options):
        self.get_changelog()

        if options['check_version']:
            self.check_schema_changelog_version()
            return

        self.setup_workspace()
        self.download_sde_export()

        if options['download_only']:
            logger.info('Download Only flag set, SDE is now downloaded and extracted.')
            return



