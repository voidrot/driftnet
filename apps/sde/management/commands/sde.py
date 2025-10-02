import logging
import sys
import zipfile
from pathlib import Path
from typing import Any

import httpx
from django.core.management.base import BaseCommand
import jsonlines
import textcase
from yaml import load

from apps.sde import app_settings
from apps.sde.models.agent_type import AgentType
from apps.sde.models.agents_in_space import AgentsInSpace
from apps.sde.models.ancestry import Ancestry
from apps.sde.models.bloodline import Bloodline
from apps.sde.models.blueprint import Blueprint
from apps.sde.models.category import Category
from apps.sde.models.certificate import Certificate
from apps.sde.models.changelog import Changelog
from apps.sde.models.character_attribute import CharacterAttribute
from apps.sde.models.contraband_type import ContrabandType
from apps.sde.models.control_tower_resource import ControlTowerResource
from apps.sde.models.corporation_activity import CorporationActivity
from apps.sde.models.dbuff_collection import DbuffCollection
from apps.sde.models.dogma_attribute import DogmaAttribute
from apps.sde.models.dogma_attribute_category import DogmaAttributeCategory
from apps.sde.models.dogma_effect import DogmaEffect
from apps.sde.models.dogma_unit import DogmaUnit
from apps.sde.models.dynamic_item_attribute import DynamicItemAttribute
from apps.sde.models.faction import Faction
from apps.sde.models.graphic import Graphic
from apps.sde.models.group import Group
from apps.sde.models.icon import Icon
from apps.sde.models.landmark import Landmark
from apps.sde.models.map_asteroid_belt import MapAsteroidBelt
from apps.sde.models.map_constellation import MapConstellation
from apps.sde.models.map_moon import MapMoon

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

    def determine_required_updates(self) -> list[dict[str, Any]]:
        pass

    def load_agents_in_space(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('agents_in_space') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = AgentsInSpace(
                    id = obj.get('_key'),
                    dungeon_id = obj.get('dungeonID'),
                    solar_system_id = obj.get('solarSystemID'),
                    spawn_point_id = obj.get('spawnPointID'),
                    type_id = obj.get('typeID'),
                )
                data.append(item)

            AgentsInSpace.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['dungeon_id', 'solar_system_id', 'spawn_point_id', 'type_id'],
                unique_fields=['id'],
            )

    def load_agent_types(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('agent_types') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = AgentType(
                    id = obj.get('_key'),
                    name = obj.get('name'),
                )
                data.append(item)
            AgentType.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name'],
                unique_fields=['id'],
            )

    def load_ancestry(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('ancestries') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Ancestry(
                    id = obj.get('_key'),
                    bloodline_id = obj.get('bloodlineID'),
                    charisma = obj.get('charisma'),
                    intelligence = obj.get('intelligence'),
                    memory = obj.get('memory'),
                    perception = obj.get('perception'),
                    willpower = obj.get('willpower'),
                    description = obj.get('description'),
                    short_description = obj.get('shortDescription'),
                    icon_id = obj.get('iconID'),
                    name = obj.get('name')
                )
                data.append(item)

            Ancestry.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['bloodline_id', 'charisma', 'intelligence', 'memory', 'perception', 'willpower', 'description', 'short_description', 'icon_id', 'name'],
                unique_fields=['id'],
            )

    def load_bloodlines(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('bloodlines') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Bloodline(
                    id = obj.get('_key'),
                    charisma = obj.get('charisma'),
                    corporation_id = obj.get('corporationID'),
                    description = obj.get('description'),
                    icon_id = obj.get('iconID'),
                    intelligence = obj.get('intelligence'),
                    memory = obj.get('memory'),
                    name = obj.get('name'),
                    perception = obj.get('perception'),
                    race_id = obj.get('raceID'),
                    willpower = obj.get('willpower'),
                )
                data.append(item)
            Bloodline.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['charisma', 'corporation_id', 'description', 'icon_id', 'intelligence', 'memory', 'name', 'perception', 'race_id', 'willpower'],
                unique_fields=['id'],
            )

    def load_blueprints(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('blueprints') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Blueprint(
                    id = obj.get('_key'),
                    activities = obj.get('activities'),
                    blueprint_type_id = obj.get('blueprintTypeID'),
                    max_production_limit = obj.get('maxProductionLimit'),
                )
                data.append(item)
            Blueprint.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['activities', 'blueprint_type_id', 'max_production_limit'],
                unique_fields=['id'],
            )

    def load_categories(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('categories') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Category(
                    id = obj.get('_key'),
                    name = obj.get('name'),
                    published = obj.get('published'),
                    icon_id = obj.get('iconID'),
                )
                data.append(item)
            Category.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name', 'published', 'icon_id'],
                unique_fields=['id'],
            )

    def load_certificates(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('certificates') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Certificate(
                    id = obj.get('_key'),
                    description = obj.get('description'),
                    group_id = obj.get('groupID'),
                    name = obj.get('name'),
                    recommended_for = obj.get('recommendedFor', []),
                    skill_types = obj.get('skillTypes', []),
                )
                data.append(item)
            Certificate.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['group_id', 'name', 'description', 'recommended_for', 'skill_types'],
                unique_fields=['id'],
            )

    def load_character_attributes(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('character_attributes') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = CharacterAttribute(
                    id = obj.get('_key'),
                    description = obj.get('description'),
                    icon_id = obj.get('iconID'),
                    name = obj.get('name'),
                    notes = obj.get('notes', ''),
                    short_description = obj.get('shortDescription', '')
                )
                data.append(item)
            CharacterAttribute.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name', 'description', 'icon_id', 'notes', 'short_description'],
                unique_fields=['id'],
            )

    def load_contraband_types(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('contraband_types') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = ContrabandType(
                    id = obj.get('_key'),
                    factions = obj.get('factions', [])
                )
                data.append(item)
            ContrabandType.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['factions'],
                unique_fields=['id'],
            )

    def load_control_tower_resources(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('control_tower_resources') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = ControlTowerResource(
                    id = obj.get('_key'),
                    resources = obj.get('resources', [])
                )
                data.append(item)
            ControlTowerResource.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['resources'],
                unique_fields=['id'],
            )

    def load_corporation_activities(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('corporation_activities') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = CorporationActivity(
                    id = obj.get('_key'),
                    name = obj.get('name'),
                )
                data.append(item)
            CorporationActivity.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name'],
                unique_fields=['id'],
            )

    def load_dbuff_collections(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('dbuff_collections') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = DbuffCollection(
                    id = obj.get('_key'),
                    aggregate_mode = obj.get('aggregateMode'),
                    developer_description = obj.get('developerDescription', ''),
                    item_modifiers = obj.get('itemModifiers', []),
                    location_group_modifiers = obj.get('locationGroupModifiers', []),
                    location_modifiers = obj.get('locationModifiers', []),
                    location_required_skill_modifiers = obj.get('locationRequiredSkillModifiers', []),
                    operation_name = obj.get('operationName', ''),
                    show_output_value_in_ui = obj.get('showOutputValueInUI', ''),
                    display_name = obj.get('displayName', {})
                )
                data.append(item)
            DbuffCollection.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['aggregate_mode', 'developer_description', 'item_modifiers', 'location_group_modifiers', 'location_modifiers', 'location_required_skill_modifiers', 'operation_name', 'show_output_value_in_ui', 'display_name'],
                unique_fields=['id'],
            )

    def load_dogma_attribute_categories(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('dogma_attribute_categories') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = DogmaAttributeCategory(
                    id = obj.get('_key'),
                    name = obj.get('name'),
                    description = obj.get('description', ''),
                )
                data.append(item)
            DogmaAttributeCategory.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name', 'description'],
                unique_fields=['id'],
            )

    def load_dogma_attributes(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('dogma_attributes') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = DogmaAttribute(
                    id = obj.get('_key'),
                    attribute_category_id = obj.get('attributeCategoryID'),
                    data_type = obj.get('dataType'),
                    default_value = obj.get('defaultValue'),
                    description = obj.get('description', ''),
                    display_when_zero = obj.get('displayWhenZero'),
                    high_is_good = obj.get('highIsGood'),
                    name = obj.get('name'),
                    published = obj.get('published'),
                    stackable = obj.get('stackable'),
                    display_name = obj.get('displayName', {}),
                    icon_id = obj.get('iconID'),
                    tooltip_description = obj.get('tooltipDescription', {}),
                    tooltip_title = obj.get('tooltipTitle', {}),
                    unit_id = obj.get('unitID'),
                    charge_recharge_time_id = obj.get('chargeRechargeTimeID'),
                    max_attribute_id = obj.get('maxAttributeID'),
                    min_attribute_id = obj.get('minAttributeID'),
                )
                data.append(item)
            DogmaAttribute.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['attribute_category_id', 'data_type', 'default_value', 'description', 'display_when_zero', 'high_is_good', 'name', 'published', 'stackable', 'display_name', 'icon_id', 'tooltip_description', 'tooltip_title', 'unit_id', 'charge_recharge_time_id', 'max_attribute_id', 'min_attribute_id'],
                unique_fields=['id'],
            )

    def load_dogma_effects(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('dogma_effects') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = DogmaEffect(
                    id = obj.get('_key'),
                    disallow_auto_repeat = obj.get('disallowAutoRepeat'),
                    discharge_attribute_id = obj.get('dischargeAttributeID'),
                    duration_attribute_id = obj.get('durationAttributeID'),
                    effect_category_id = obj.get('effectCategoryID'),
                    electronic_chance = obj.get('electronicChance'),
                    guid = obj.get('guid', ''),
                    is_assistance = obj.get('isAssistance'),
                    is_offensive = obj.get('isOffensive'),
                    is_warp_safe = obj.get('isWarpSafe'),
                    name = obj.get('name'),
                    propulsion_chance = obj.get('propulsionChance'),
                    published = obj.get('published'),
                    range_chance = obj.get('rangeChance'),
                    distribution = obj.get('distribution'),
                    falloff_attribute_id = obj.get('falloffAttributeID'),
                    range_attribute_id = obj.get('rangeAttributeID'),
                    tracking_speed_attribute_id = obj.get('trackingSpeedAttributeID'),
                    description = obj.get('description', {}),
                    display_name = obj.get('displayName', {}),
                    icon_id = obj.get('iconID'),
                    modifier_info = obj.get('modifierInfo', []),
                    npc_usage_chance_attribute_id = obj.get('npcUsageChanceAttributeID'),
                    npc_activation_chance_attribute_id = obj.get('npcActivationChanceAttributeID'),
                    fitting_usage_chance_attribute_id = obj.get('fittingUsageChanceAttributeID'),
                    resistance_attribute_id = obj.get('resistanceAttributeID'),
                )
                data.append(item)
            DogmaEffect.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['disallow_auto_repeat', 'discharge_attribute_id', 'duration_attribute_id', 'effect_category_id', 'electronic_chance', 'guid', 'is_assistance', 'is_offensive', 'is_warp_safe', 'name', 'propulsion_chance', 'published', 'range_chance', 'distribution', 'falloff_attribute_id', 'range_attribute_id', 'tracking_speed_attribute_id', 'description', 'display_name', 'icon_id', 'modifier_info', 'npc_usage_chance_attribute_id', 'npc_activation_chance_attribute_id', 'fitting_usage_chance_attribute_id', 'resistance_attribute_id'],
                unique_fields=['id'],
            )

    def load_dogma_units(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('dogma_units') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = DogmaUnit(
                    id = obj.get('_key'),
                    name = obj.get('name'),
                    description = obj.get('description', ''),
                    display_name = obj.get('displayName', {}),
                )
                data.append(item)
            DogmaUnit.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name', 'description', 'display_name'],
                unique_fields=['id'],
            )

    def load_dynamic_item_attributes(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('dynamic_item_attributes') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = DynamicItemAttribute(
                    id = obj.get('_key'),
                    attribute_ids = obj.get('attributeIDs', []),
                    input_output_mapping = obj.get('inputOutputMapping', {}),
                )
                data.append(item)
            DynamicItemAttribute.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['attribute_ids', 'input_output_mapping'],
                unique_fields=['id'],
            )

    def load_factions(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('factions') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Faction(
                    id = obj.get('_key'),
                    corporation_id = obj.get('corporationID'),
                    description = obj.get('description', ''),
                    flat_logo = obj.get('flatLogo', ''),
                    flat_logo_with_name = obj.get('flatLogoWithName', ''),
                    icon_id = obj.get('iconID'),
                    member_races = obj.get('memberRaces', []),
                    militia_corporation_id = obj.get('militiaCorporationID'),
                    name = obj.get('name'),
                    short_description = obj.get('shortDescription', ''),
                    size_factor = obj.get('sizeFactor'),
                    solar_system_id = obj.get('solarSystemID'),
                    unique_name = obj.get('uniqueName')
                )
                data.append(item)
            Faction.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['corporation_id', 'description', 'flat_logo', 'flat_logo_with_name', 'icon_id', 'member_races', 'militia_corporation_id', 'name', 'short_description', 'size_factor', 'solar_system_id', 'unique_name'],
                unique_fields=['id'],
            )

    def load_graphics(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('graphics') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Graphic(
                    id = obj.get('_key'),
                    graphic_file = obj.get('graphicFile', ''),
                    icon_folder = obj.get('iconFolder', ''),
                    sof_faction_name = obj.get('sofFactionName', ''),
                    sof_hull_name = obj.get('sofHullName', ''),
                    sof_race_name = obj.get('sofRaceName', ''),
                    sof_material_set_id = obj.get('sofMaterialSetID'),
                    sof_layout = obj.get('sofLayout', ''),
                )
                data.append(item)
            Graphic.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['graphic_file', 'icon_folder', 'sof_faction_name', 'sof_hull_name', 'sof_race_name', 'sof_material_set_id', 'sof_layout'],
                unique_fields=['id'],
            )

    def load_groups(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('groups') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Group(
                    id = obj.get('_key'),
                    anchorable = obj.get('anchorable'),
                    anchored = obj.get('anchored'),
                    category_id = obj.get('categoryID'),
                    fittable_non_singleton = obj.get('fittableNonSingleton'),
                    name = obj.get('name'),
                    published = obj.get('published'),
                    use_base_price = obj.get('useBasePrice'),
                    icon_id = obj.get('iconID'),
                )
                data.append(item)
            Group.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['anchorable', 'anchored', 'category_id', 'fittable_non_singleton', 'name', 'published', 'use_base_price', 'icon_id'],
                unique_fields=['id'],
            )

    def load_icons(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('icons') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Icon(
                    id = obj.get('_key'),
                    icon_file = obj.get('iconFile', ''),
                )
                data.append(item)
            Icon.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['icon_file'],
                unique_fields=['id'],
            )

    def load_landmarks(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('landmarks') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = Landmark(
                    id = obj.get('_key'),
                    name = obj.get('name'),
                    description = obj.get('description', ''),
                    position = obj.get('position', {}),
                    icon_id = obj.get('iconID'),
                    location_id = obj.get('locationID'),
                )
                data.append(item)
            Landmark.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['name', 'description', 'position', 'icon_id', 'location_id'],
                unique_fields=['id'],
            )

    def load_map_asteroid_belts(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('map_asteroid_belts') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = MapAsteroidBelt(
                    id = obj.get('_key'),
                    celestial_index = obj.get('celestialIndex'),
                    orbit_id = obj.get('orbitID'),
                    orbit_index = obj.get('orbitIndex'),
                    position = obj.get('position', {}),
                    radius = obj.get('radius'),
                    solar_system_id = obj.get('solarSystemID'),
                    type_id = obj.get('typeID'),
                    unique_name = obj.get('uniqueName', ''),
                )
                data.append(item)
            MapAsteroidBelt.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['celestial_index', 'orbit_id', 'orbit_index', 'position', 'radius', 'solar_system_id', 'type_id', 'unique_name'],
                unique_fields=['id'],
            )

    def load_map_constellations(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('map_constellations') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = MapConstellation(
                    id = obj.get('_key'),
                    faction_id = obj.get('factionID'),
                    name = obj.get('name'),
                    position = obj.get('position', {}),
                    region_id = obj.get('regionID'),
                    solar_system_ids = obj.get('solarSystemIDs', []),
                    wormhole_class_id = obj.get('wormholeClassID'),
                )
                data.append(item)
            MapConstellation.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['faction_id', 'name', 'position', 'region_id', 'solar_system_ids', 'wormhole_class_id'],
                unique_fields=['id'],
            )

    def load_map_moons(self) -> None:
        with jsonlines.open(self.workspace_dir / 'extracted' / str(textcase.camel('map_moons') + '.jsonl')) as reader:
            data = []

            for obj in reader:
                item = MapMoon(
                    id = obj.get('_key'),
                    attributes = obj.get('attributes', {}),
                    celestial_index = obj.get('celestialIndex'),
                    orbit_id = obj.get('orbitID'),
                    orbit_index = obj.get('orbitIndex'),
                    position = obj.get('position', {}),
                    radius = obj.get('radius'),
                    solar_system_id = obj.get('solarSystemID'),
                    statistics = obj.get('statistics', {}),
                    type_id = obj.get('typeID'),
                    npc_station_ids = obj.get('npcStationIDs', []),
                    unique_name = obj.get('uniqueName', ''),
                )
                data.append(item)
            MapMoon.objects.bulk_create(
                data,
                update_conflicts=True,
                update_fields=['attributes', 'celestial_index', 'orbit_id', 'orbit_index', 'position', 'radius', 'solar_system_id', 'statistics', 'type_id', 'unique_name', 'npc_station_ids'],
                unique_fields=['id'],
            )

    def load_data_to_models(self) -> None:
        self.load_agents_in_space()
        self.load_agent_types()
        self.load_ancestry()
        self.load_bloodlines()
        self.load_blueprints()
        self.load_categories()
        self.load_certificates()
        self.load_character_attributes()
        self.load_contraband_types()
        self.load_control_tower_resources()
        self.load_corporation_activities()
        self.load_dbuff_collections()
        self.load_dogma_attribute_categories()
        self.load_dogma_attributes()
        self.load_dogma_effects()
        self.load_dogma_units()
        self.load_dynamic_item_attributes()
        self.load_factions()
        self.load_graphics()
        self.load_groups()
        self.load_icons()
        self.load_landmarks()
        self.load_map_asteroid_belts()
        self.load_map_constellations()
        self.load_map_moons()

    def handle(self, *args, **options) -> None:
        self.get_changelog()

        if options['check_version']:
            self.check_schema_changelog_version()
            return

        self.setup_workspace()

        if not options['skip_download']:
            self.download_sde_export()

        if options['download_only']:
            logger.info('Download Only flag set, SDE is now downloaded and extracted.')
            return

        self.load_data_to_models()

