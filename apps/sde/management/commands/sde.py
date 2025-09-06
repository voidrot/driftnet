import argparse
import hashlib
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import zipfile

import httpx
from django.conf import settings
from django.core.management.base import BaseCommand
from apps.sde.models import Checksum
import subprocess
from pathlib import Path as _Path

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Perform SDE tasks'

    workspace_dir = Path(settings.SDE_WORKSPACE)
    local_checksums = {}
    remote_checksums = {}

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            '--force-download',
            action='store_true',
            help='Force fresh download and import of the SDE',
        )

        parser.add_argument(
            '--skip-yaml-to-json',
            action='store_true',
            help='Skip the YAML to JSON conversion step',
        )

        parser.add_argument(
            '--download-only',
            action='store_true',
            help='Only download the SDE and extract, skip further processing',
        )

    # Setup the SDE workspace
    def setup_workspace(self) -> None:
        logger.info('Setting up workspace for SDE tasks')
        self.workspace_dir.mkdir(parents=True, exist_ok=True)

    # Query ESI remote endpoint for file checksums
    def get_remote_checksums(self):
        if not self.remote_checksums:
            res = httpx.get(settings.SDE_CHECKSUM_URL)
            if res.status_code == 200:
                for line in res.text.splitlines():
                    checksum, name = line.strip().split()
                    self.remote_checksums[name] = checksum

    # Query the local database for file checksums that are active in the database
    def get_local_checksums(self):
        checksums = Checksum.objects.all()
        self.local_checksums = {cs.name: cs.checksum for cs in checksums}

    # Lookup a checksum of applied files
    def local_checksum_lookup(self, name: str) -> str:
        return dict(self.local_checksums).get(name, '')

    # lookup the latest checksum of remote files
    def remote_checksum_lookup(self, name: str) -> str:
        return self.remote_checksums.get(name, '')

    def validate_checksum(self, name: str) -> bool:
        local_checksum = self.local_checksum_lookup(name)
        remote_checksum = self.remote_checksum_lookup(name)
        if local_checksum != remote_checksum:
            logger.warning(
                f'Checksum mismatch for {name} - local: {local_checksum}, remote: {remote_checksum}'
            )
            return False
        logger.info(f'Checksum match for {name} - {local_checksum}')
        return True

    # validate SDE zip checksum
    def validate_sde_zip_checksum(self) -> bool:
        logger.info('Validating SDE zip checksum')
        md5_hash = hashlib.md5(usedforsecurity=False)
        try:
            with zipfile.ZipFile(
                self.workspace_dir / 'sde.zip', 'r', zipfile.ZIP_DEFLATED
            ) as z:
                file_name = z.namelist()
                for f in file_name:
                    md5_hash.update(z.read(f))
        except zipfile.BadZipFile:
            logger.exception('Bad zip file')
            return False

        checksum = md5_hash.hexdigest()
        remote_checksum = self.remote_checksum_lookup('sde.zip')
        if checksum != remote_checksum:
            logger.error(
                f'SDE checksum failed - got {checksum}, expected {remote_checksum}'
            )
            return False
        else:
            logger.info(f'SDE checksum passed for {checksum}')
            Checksum.objects.update_or_create(
                name='sde.zip',
                checksum=checksum,
            )
            return True

    # Download the SDE data
    def download_sde(self, force_download: bool) -> None:
        needs_download = False
        if Path(self.workspace_dir / 'sde.zip').exists() and not force_download:
            logger.info('SDE zip already exists, validating checksums...')
            if not self.validate_sde_zip_checksum():
                logger.info('SDE zip checksum is invalid, re-downloading...')
                needs_download = True
        else:
            needs_download = True

        logger.info('Downloading SDE data...')
        # Implement the download logic here
        if force_download or needs_download:
            logger.info('Forcing fresh download of SDE')
            Path(self.workspace_dir / 'sde.zip').unlink(missing_ok=True)
            # Implement the download logic here
            chunk_size = 1 * 1024**2
            with (
                httpx.stream('GET', settings.SDE_ARCHIVE_URL) as r,
                Path(self.workspace_dir / 'sde.zip').open('wb') as f,
            ):
                for chunk in r.iter_bytes(chunk_size=chunk_size):
                    f.write(chunk)
            self.validate_sde_zip_checksum()
            logger.info(
                f'SDE archive downloaded to {Path(self.workspace_dir / "sde.zip").absolute().resolve()}'
            )

    def extract_sde(self) -> None:
        with zipfile.ZipFile(self.workspace_dir / 'sde.zip', 'r') as z:
            z.extractall(self.workspace_dir)

    def run_yaml_to_json_conversion(self) -> None:
        """Run the repository script that converts SDE YAML files to JSON.

        The script lives at scripts/convert-sde-yaml-to-json.sh in the repo root.
        Prefer settings.BASE_DIR when available, otherwise fall back to cwd.
        """
        repo_root = Path(getattr(settings, 'BASE_DIR', _Path.cwd()))
        script_path = repo_root / 'scripts' / 'convert-sde-yaml-to-json.sh'
        if not script_path.exists():
            logger.warning(
                'Conversion script not found at %s, skipping YAML->JSON conversion',
                script_path,
            )
            return

        cmd = [str(script_path), str(self.workspace_dir)]
        logger.info('Running YAML->JSON conversion script: %s', ' '.join(cmd))
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        except Exception:
            logger.exception('Failed to run conversion script')
            return

        if res.stdout:
            logger.debug('Conversion stdout: %s', res.stdout)
        if res.stderr:
            logger.warning('Conversion stderr: %s', res.stderr)

        if res.returncode != 0:
            logger.error('Conversion script failed with exit code %s', res.returncode)
        else:
            logger.info('YAML->JSON conversion completed successfully')

    def handle(self, *args: Any, **options: Any) -> None:
        # Setup the workspace
        self.setup_workspace()
        self.get_local_checksums()
        self.get_remote_checksums()
        # Validate and Download the SDE data
        self.download_sde(force_download=options.get('force_download', False))
        self.extract_sde()
        # Convert extracted YAML files to JSON (optional script)
        if not options.get('skip_yaml_to_json', False):
            self.run_yaml_to_json_conversion()
        if options.get('download_only', False):
            logger.info('Download-only flag set, skipping further processing')
            return
        # logger.info(self.local_checksums)
        # logger.info(self.remote_checksums)
