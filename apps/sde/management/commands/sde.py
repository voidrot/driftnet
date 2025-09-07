import argparse
import hashlib
import json
import logging
import subprocess
import zipfile
from pathlib import Path
from pathlib import Path as _Path
from typing import Any

import httpx
from django.conf import settings
from django.core.management.base import BaseCommand

from apps.sde.models import Checksum
from apps.sde.models.agents import Agent
from apps.sde.models.agents_in_space import AgentsInSpace
from apps.sde.models.ancestries import Ancestry
from apps.sde.models.bloodlines import Bloodline
from apps.sde.models.blueprints import Blueprint
from apps.sde.models.categories import Category
from apps.sde.models.certificates import Certificate
from apps.sde.models.character_attributes import CharacterAttribute
from apps.sde.models.contraband_types import ContrabandType
from apps.sde.models.control_tower_resources import ControlTowerResource
from apps.sde.models.inv_flags import InvFlag
from apps.sde.models.inv_items import InvItem
from apps.sde.models.inv_names import InvName
from apps.sde.models.inv_positions import InvPosition
from apps.sde.models.inv_unique_names import InvUniqueName
from apps.sde.models.sta_stations import StaStation

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

    def get_file_checksum(self, file_path: Path) -> str:
        """Calculate the MD5 checksum of a file."""
        # Ensure we have a Path object and the file exists
        path = Path(file_path)
        if not path.exists() or not path.is_file():
            logger.warning('File for checksum not found or not a file: %s', path)
            return ''

        md5_hash = hashlib.md5()
        try:
            # Read and update hash string value in blocks (8K buffer)
            with path.open('rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    md5_hash.update(chunk)
        except Exception:
            logger.exception('Failed calculating checksum for %s', path)
            return ''

        return md5_hash.hexdigest()

    def build_file_path(self, sub_path: str, filename: str) -> tuple[Path, Path]:
        filename_base = filename.rsplit('.', 1)[0]  # Remove extension if present
        return (
            Path(settings.SDE_WORKSPACE / sub_path / f'{filename_base}.json'),
            Path(settings.SDE_WORKSPACE / sub_path / f'{filename_base}.yaml'),
        )

    def load_bsd_inv_flags(self) -> None:
        logger.info('Loading invFlags from BSD data...')
        json_file, yaml_file = self.build_file_path('bsd', 'invFlags')
        existing_checksum = self.local_checksum_lookup('bsd/invFlags.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('invFlags.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for item in data:
                    InvFlag(
                        flag_id=item.get('flagID'),
                        flag_name=item.get('flagName'),
                        flag_text=item.get('flagText'),
                        order_id=item.get('orderID'),
                    ).save()
        except Exception:
            logger.exception('Failed loading invFlags from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='bsd/invFlags.yaml',
            checksum=checksum,
        )

    def load_bsd_inv_items(self) -> None:
        logger.info('Loading invItems from BSD data...')
        json_file, yaml_file = self.build_file_path('bsd', 'invItems')
        existing_checksum = self.local_checksum_lookup('bsd/invItems.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('invItems.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for item in data:
                    InvItem(
                        item_id=item.get('itemID'),
                        flag_id=item.get('flagID'),
                        location_id=item.get('locationID'),
                        owner_id=item.get('ownerID'),
                        quantity=item.get('quantity'),
                        type_id=item.get('typeID'),
                    ).save()
        except Exception:
            logger.exception('Failed loading invItems from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='bsd/invItems.yaml',
            checksum=checksum,
        )

    def load_bsd_inv_names(self) -> None:
        logger.info('Loading invNames from BSD data...')
        json_file, yaml_file = self.build_file_path('bsd', 'invNames')
        existing_checksum = self.local_checksum_lookup('bsd/invNames.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('invNames.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for item in data:
                    InvName(
                        item_id=item.get('itemID'),
                        item_name=item.get('itemName'),
                    ).save()
        except Exception:
            logger.exception('Failed loading invNames from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='bsd/invNames.yaml',
            checksum=checksum,
        )

    def load_bsd_inv_positions(self) -> None:
        logger.info('Loading invPositions from BSD data...')
        json_file, yaml_file = self.build_file_path('bsd', 'invPositions')
        existing_checksum = self.local_checksum_lookup('bsd/invPositions.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('invPositions.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for item in data:
                    InvPosition(
                        item_id=item.get('itemID'),
                        pitch=item.get('pitch'),
                        roll=item.get('roll'),
                        yaw=item.get('yaw'),
                        x=item.get('x'),
                        y=item.get('y'),
                        z=item.get('z'),
                    ).save()
        except Exception:
            logger.exception('Failed loading invPositions from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='bsd/invPositions.yaml',
            checksum=checksum,
        )

    def load_bsd_inv_unique_names(self) -> None:
        logger.info('Loading invUniqueNames from BSD data...')
        json_file, yaml_file = self.build_file_path('bsd', 'invUniqueNames')
        existing_checksum = self.local_checksum_lookup('bsd/invUniqueNames.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('invUniqueNames.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for item in data:
                    InvUniqueName(
                        item_id=item.get('itemID'),
                        group_id=item.get('groupID'),
                        item_name=item.get('itemName'),
                    ).save()
        except Exception:
            logger.exception('Failed loading invUniqueNames from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='bsd/invUniqueNames.yaml',
            checksum=checksum,
        )

    def load_bsd_sta_stations(self) -> None:
        logger.info('Loading staStations from BSD data...')
        json_file, yaml_file = self.build_file_path('bsd', 'staStations')
        existing_checksum = self.local_checksum_lookup('bsd/staStations.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('staStations.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for item in data:
                    StaStation(
                        station_id=item.get('stationID'),
                        security=item.get('security'),
                        station_type_id=item.get('stationTypeID'),
                        corporation_id=item.get('corporationID'),
                        solar_system_id=item.get('solarSystemID'),
                        constellation_id=item.get('constellationID'),
                        region_id=item.get('regionID'),
                        station_name=item.get('stationName'),
                        x=item.get('x'),
                        y=item.get('y'),
                        z=item.get('z'),
                        reprocessing_efficiency=item.get('reprocessingEfficiency'),
                        reprocessing_stations_take=item.get('reprocessingStationsTake'),
                        reprocessing_hangar_flag=item.get('reprocessingHangarFlag'),
                        docking_cost_per_volume=item.get('dockingCostPerVolume'),
                        max_ship_volume_dockable=item.get('maxShipVolumeDockable'),
                        office_rental_cost=item.get('officeRentalCost'),
                        operation_id=item.get('operationID'),
                    ).save()
        except Exception:
            logger.exception('Failed loading staStations from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='bsd/staStations.yaml',
            checksum=checksum,
        )

    def load_fsd_agents(self) -> None:
        logger.info('Loading agents from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'agents')
        existing_checksum = self.local_checksum_lookup('fsd/agents.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('agents.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    Agent(
                        id=k,
                        agent_type_id=v.get('agentTypeID'),
                        corporation_id=v.get('corporationID'),
                        division_id=v.get('divisionID'),
                        is_locator=v.get('isLocator'),
                        level=v.get('level'),
                        location_id=v.get('locationID'),
                    ).save()
        except Exception:
            logger.exception('Failed loading agents from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/agents.yaml',
            checksum=checksum,
        )

    def load_fsd_agents_in_space(self) -> None:
        logger.info('Loading agentsInSpace from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'agentsInSpace')
        existing_checksum = self.local_checksum_lookup('fsd/agentsInSpace.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('agentsInSpace.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    AgentsInSpace(
                        id=k,
                        dungeon_id=v.get('dungeonID'),
                        solar_system_id=v.get('solarSystemID'),
                        spawn_point_id=v.get('spawnPointID'),
                        type_id=v.get('typeID'),
                    ).save()
        except Exception:
            logger.exception('Failed loading agentsInSpace from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/agentsInSpace.yaml',
            checksum=checksum,
        )

    def load_fsd_ancestries(self) -> None:
        logger.info('Loading ancestries from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'ancestries')
        existing_checksum = self.local_checksum_lookup('fsd/ancestries.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('ancestries.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    Ancestry(
                        id=k,
                        bloodline_id=v.get('bloodlineID'),
                        charisma=v.get('charisma'),
                        description_id=v.get('descriptionID'),
                        icon_id=v.get('iconID'),
                        intelligence=v.get('intelligence'),
                        memory=v.get('memory'),
                        name_id=v.get('nameID'),
                        perception=v.get('perception'),
                        short_description=v.get('shortDescription'),
                        willpower=v.get('willpower'),
                    ).save()
        except Exception:
            logger.exception('Failed loading ancestries from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/ancestries.yaml',
            checksum=checksum,
        )

    def load_fsd_bloodlines(self) -> None:
        logger.info('Loading bloodlines from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'bloodlines')
        existing_checksum = self.local_checksum_lookup('fsd/bloodlines.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('bloodlines.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    Bloodline(
                        id=k,
                        charisma=v.get('charisma'),
                        corporation_id=v.get('corporationID'),
                        description_id=v.get('descriptionID'),
                        icon_id=v.get('iconID'),
                        intelligence=v.get('intelligence'),
                        memory=v.get('memory'),
                        name_id=v.get('nameID'),
                        perception=v.get('perception'),
                        race_id=v.get('raceID'),
                        willpower=v.get('willpower'),
                    ).save()
        except Exception:
            logger.exception('Failed loading bloodlines from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/bloodlines.yaml',
            checksum=checksum,
        )

    def load_fsd_blueprints(self) -> None:
        logger.info('Loading blueprints from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'blueprints')
        existing_checksum = self.local_checksum_lookup('fsd/blueprints.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('blueprints.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    Blueprint(
                        id=k,
                        actibities=v.get('activities'),
                        blueprint_type_id=v.get('blueprintTypeID'),
                        max_production_limit=v.get('maxProductionLimit'),
                    ).save()
        except Exception:
            logger.exception('Failed loading blueprints from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/blueprints.yaml',
            checksum=checksum,
        )

    def load_fsd_categories(self) -> None:
        logger.info('Loading categories from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'categories')
        existing_checksum = self.local_checksum_lookup('fsd/categories.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('categories.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    Category(
                        id=k,
                        name=v.get('name'),
                        published=v.get('published'),
                        icon_id=v.get('iconID'),
                    ).save()
        except Exception:
            logger.exception('Failed loading categories from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/categories.yaml',
            checksum=checksum,
        )
    
    def load_fsd_certificates(self) -> None:
        logger.info('Loading certificates from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'certificates')
        existing_checksum = self.local_checksum_lookup('fsd/certificates.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('certificates.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    Certificate(
                        id=k,
                        description=v.get('description'),
                        group_id=v.get('groupID'),
                        name=v.get('name'),
                        recommended_for=v.get('recommendedFor'),
                        skill_types=v.get('skillTypes'),
                    ).save()
        except Exception:
            logger.exception('Failed loading certificates from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/certificates.yaml',
            checksum=checksum,
        )
        
    def load_fsd_character_attributes(self) -> None:
        logger.info('Loading characterAttributes from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'characterAttributes')
        existing_checksum = self.local_checksum_lookup('fsd/characterAttributes.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('characterAttributes.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    CharacterAttribute(
                        id=k,
                        description=v.get('description'),
                        icon_id=v.get('iconID'),
                        name_id=v.get('nameID'),
                        notes=v.get('notes'),
                        short_description=v.get('shortDescription'),
                    ).save()
        except Exception:
            logger.exception('Failed loading characterAttributes from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/characterAttributes.yaml',
            checksum=checksum,
        )
        
    def load_fsd_contraband_types(self) -> None:
        logger.info('Loading contrabandTypes from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'contrabandTypes')
        existing_checksum = self.local_checksum_lookup('fsd/contrabandTypes.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('contrabandTypes.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    ContrabandType(
                        id=k,
                        factions=v.get('factions'),
                    ).save()
        except Exception:
            logger.exception('Failed loading contrabandTypes from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/contrabandTypes.yaml',
            checksum=checksum,
        )
    
    def load_fsd_control_tower_resources(self) -> None:
        logger.info('Loading controlTowerResources from FSD data...')
        json_file, yaml_file = self.build_file_path('fsd', 'controlTowerResources')
        existing_checksum = self.local_checksum_lookup('fsd/controlTowerResources.yaml')
        checksum = self.get_file_checksum(yaml_file)
        if existing_checksum == checksum and existing_checksum != '':
            logger.info('controlTowerResources.yaml checksum matches existing, skipping load')
            return
        try:
            with Path(json_file).open() as f:
                data = json.load(f)
                for k, v in data:
                    ControlTowerResource(
                        id=k,
                        resources=v.get('resources'),
                    ).save()
        except Exception:
            logger.exception('Failed loading controlTowerResources from %s', json_file)
            return
        Checksum.objects.update_or_create(
            name='fsd/controlTowerResources.yaml',
            checksum=checksum,
        )

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
        # Load data into the database
        ## Load BSD data
        self.load_bsd_inv_flags()
        self.load_bsd_inv_items()
        self.load_bsd_inv_names()
        self.load_bsd_inv_positions()
        self.load_bsd_inv_unique_names()
        self.load_bsd_sta_stations()
        ## Load FSD data
        self.load_fsd_agents()
        self.load_fsd_agents_in_space()
        self.load_fsd_ancestries()
        self.load_fsd_bloodlines()
        self.load_fsd_blueprints()
        self.load_fsd_categories()
        self.load_fsd_certificates()
        self.load_fsd_character_attributes()
        self.load_fsd_contraband_types()
        self.load_fsd_control_tower_resources()

        logger.info('SDE processing completed')
