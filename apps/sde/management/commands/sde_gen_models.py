import contextlib
import json
import logging
import re
from pathlib import Path

import inflect
from django.conf import settings
from django.core.management.base import BaseCommand
from django.template import Context
from django.template import Template

from apps.sde import app_settings

from .helpers import INIT_MODEL_TEMPLATE
from .helpers import MODEL_INDEX_RULES
from .helpers import MODEL_PRIMARY_KEY_ID_OVERRIDE
from .helpers import MODEL_TEMPLATE
from .helpers import UNIVERSE_LOOKUP_TEMPLATE
from .helpers import collect_files

with contextlib.suppress(ImportError):
    pass

logger = logging.getLogger(__name__)
p = inflect.engine()


class Command(BaseCommand):
    help = 'Generate SDE models'

    universe_files = []
    bsd_files = []
    fsd_files = []

    def collect_all_files(self):
        self.universe_files = collect_files(
            Path(app_settings.SDE_WORKSPACE / 'universe')
        )
        self.bsd_files = collect_files(Path(app_settings.SDE_WORKSPACE / 'bsd'))
        self.fsd_files = collect_files(Path(app_settings.SDE_WORKSPACE / 'fsd'))

        ignored_files = ['translationLanguages.json']

        # Filter out ignored files
        self.universe_files = [
            f for f in self.universe_files if f.name not in ignored_files
        ]
        self.bsd_files = [f for f in self.bsd_files if f.name not in ignored_files]
        self.fsd_files = [f for f in self.fsd_files if f.name not in ignored_files]

    def convert_to_snake_case(self, name):
        """Convert a string to snake_case."""
        if isinstance(name, int):
            return name
        s = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
        return s.lower()

    def convert_to_pascal_case(self, name):
        """Convert a string to PascalCase."""
        if isinstance(name, int):
            return name
        return ''.join(word.title() for word in name.split('_'))

    def is_complex_type(self, field_type):
        """Check if the field type is complex."""
        return isinstance(field_type, (list, dict))

    def convert_to_singular_noun(self, name):
        """Convert a string to singular noun."""
        word = p.singular_noun(name)
        if not word:
            logger.warning(f'Failed to convert {name} to singular noun.')
            return name
        return word

    def extract_fields(self, data, model_name):  # noqa: C901, PLR0912
        fields = {}
        field_types = {}
        field_found = {}
        int_field_ranges = {}

        converted_data = []

        if isinstance(data, list):
            converted_data = data
        elif isinstance(data, dict):
            for item in data.items():
                converted_data.append(item[1])
        else:
            logger.warning(f'Unsupported data type: {type(data)}')
            return fields

        for item in converted_data:
            for key, value in item.items():
                field_name = self.convert_to_snake_case(key)

                if field_name not in field_found:
                    field_types[field_name] = []
                    field_found[field_name] = 1
                    if isinstance(value, int):
                        int_field_ranges[field_name] = [value, value]
                else:
                    field_found[field_name] += 1
                    if isinstance(value, int):
                        if field_name in int_field_ranges:
                            int_field_ranges[field_name][0] = min(
                                int_field_ranges[field_name][0], value
                            )
                            int_field_ranges[field_name][1] = max(
                                int_field_ranges[field_name][1], value
                            )
                        else:
                            int_field_ranges[field_name] = [value, value]
                if type(value).__name__ not in field_types[field_name]:
                    field_types[field_name].append(type(value).__name__)

        # Postgres integer range: -2147483648 to 2147483647
        pg_int_min = -2147483648
        pg_int_max = 2147483647

        type_map = {
            'int': (
                'models.IntegerField(default=None, null=True)',
                'models.IntegerField()',
            ),
            'bigint': (
                'models.BigIntegerField(default=None, null=True)',
                'models.BigIntegerField()',
            ),
            'float': (
                'models.FloatField(default=None, null=True)',
                'models.FloatField()',
            ),
            'str': ('models.TextField(default=None, null=True)', 'models.TextField()'),
            'bool': (
                'models.BooleanField(default=False, null=True)',
                'models.BooleanField()',
            ),
            'list': ('models.JSONField(default=list, null=True)', 'models.JSONField()'),
            'dict': ('models.JSONField(default=dict, null=True)', 'models.JSONField()'),
        }

        for field_name, field_values in field_types.items():
            is_optional = field_found[field_name] != len(converted_data)
            logging.debug(
                f'optional: {is_optional} | {field_name}: {field_found[field_name]} vs {len(converted_data)}'
            )
            chosen_type = None
            if len(field_values) > 1:
                if 'float' in field_values:
                    chosen_type = 'float'
                if 'int' in field_values and 'str' in field_values:
                    chosen_type = 'str'
            else:
                chosen_type = field_values[0]

            # Determine if int or bigint is needed
            if chosen_type == 'int' and field_name in int_field_ranges:
                min_val, max_val = int_field_ranges[field_name]
                if min_val < pg_int_min or max_val > pg_int_max:
                    chosen_type = 'bigint'

            for py_type, (optional_field, required_field) in type_map.items():
                if py_type == chosen_type:
                    if model_name in MODEL_PRIMARY_KEY_ID_OVERRIDE:
                        if field_name == MODEL_PRIMARY_KEY_ID_OVERRIDE[model_name]:
                            fields[field_name] = (
                                required_field.split('(')[0] + '(primary_key=True)'
                            )
                            break
                    fields[field_name] = (
                        optional_field if is_optional else required_field
                    )

        return fields

    def gen_fsd_models(self):
        for fsd_file in self.fsd_files:
            fields = {}
            logger.info(f'Processing FSD file: {fsd_file.parts[-1]}')
            model_file_name = self.convert_to_snake_case(
                fsd_file.parts[-1].replace('.json', '')
            )
            with Path(fsd_file).open('r', encoding='utf-8') as f:
                fields = self.extract_fields(json.load(f), model_file_name)
            self.gen_model_file(model_file_name, fields)

    def gen_bsd_models(self):
        for bsd_file in self.bsd_files:
            fields = {}
            logger.info(f'Processing BSD file: {bsd_file.parts[-1]}')
            model_file_name = self.convert_to_snake_case(
                bsd_file.parts[-1].replace('.json', '')
            )
            with Path(bsd_file).open('r', encoding='utf-8') as f:
                fields = self.extract_fields(json.load(f), model_file_name)
            self.gen_model_file(model_file_name, fields)

    def gen_universe_models(self):  # noqa: C901, PLR0912, PLR0915
        # Build files into single objects
        region_collection = []
        constellation_collection = []
        solar_system_collection = []
        landmark_collection = []
        planets_collection = []
        moons_collection = []
        stars_collection = []
        stargates_collection = []
        astroid_belts_collection = []

        for universe_file in self.universe_files:
            if universe_file.parts[-1] == 'region.json':
                with Path(universe_file).open('r', encoding='utf-8') as f:
                    region_collection.append(json.load(f))
            elif universe_file.parts[-1] == 'constellation.json':
                with Path(universe_file).open('r', encoding='utf-8') as f:
                    constellation_collection.append(json.load(f))
            elif universe_file.parts[-1] == 'solarsystem.json':
                with Path(universe_file).open('r', encoding='utf-8') as f:
                    solar_system_data = json.load(f)
                    planets = solar_system_data.get('planets', {})
                    for k, v in planets.items():
                        moons = v.get('moons', {})
                        if len(moons) > 0:
                            for mv in moons.values():
                                moons_collection.append(mv)  # noqa: PERF402
                            del planets[k]['moons']
                        astroid_belts = v.get('asteroidBelts', {})
                        if len(astroid_belts) > 0:
                            for av in astroid_belts.values():
                                astroid_belts_collection.append(av)  # noqa: PERF402
                            del planets[k]['asteroidBelts']
                        planets_collection.append(v)
                    del solar_system_data['planets']
                    if 'star' in solar_system_data:
                        stars_collection.append(solar_system_data.get('star', {}))
                        del solar_system_data['star']
                    if 'stargates' in solar_system_data:
                        for sgv in solar_system_data.get('stargates', {}).values():
                            stargates_collection.append(sgv)  # noqa: PERF402
                        del solar_system_data['stargates']
                    solar_system_collection.append(solar_system_data)
            elif universe_file.parts[-1] == 'landmarks.json':
                with Path(universe_file).open('r', encoding='utf-8') as f:
                    landmark_collection = json.load(f)

        # Generate region model
        model_file_name = self.convert_to_snake_case('regions')
        region_fields = self.extract_fields(region_collection, model_file_name)
        self.gen_model_file(model_file_name, region_fields)
        # generate constellation model
        model_file_name = self.convert_to_snake_case('constellations')
        constellation_fields = self.extract_fields(
            constellation_collection, model_file_name
        )
        self.gen_model_file(model_file_name, constellation_fields)
        # generate solar system model
        model_file_name = self.convert_to_snake_case('solarSystems')
        solar_system_fields = self.extract_fields(
            solar_system_collection, model_file_name
        )
        self.gen_model_file(model_file_name, solar_system_fields)
        # generate planet model
        model_file_name = self.convert_to_snake_case('planets')
        planet_fields = self.extract_fields(planets_collection, model_file_name)
        self.gen_model_file(model_file_name, planet_fields)
        # generate moon model
        model_file_name = self.convert_to_snake_case('moons')
        moon_fields = self.extract_fields(moons_collection, model_file_name)
        self.gen_model_file(model_file_name, moon_fields)
        # generate star model
        model_file_name = self.convert_to_snake_case('stars')
        star_fields = self.extract_fields(stars_collection, model_file_name)
        self.gen_model_file(model_file_name, star_fields)
        # generate stargate model
        model_file_name = self.convert_to_snake_case('stargates')
        stargate_fields = self.extract_fields(stargates_collection, model_file_name)
        self.gen_model_file(model_file_name, stargate_fields)
        # generate asteroid belt model
        model_file_name = self.convert_to_snake_case('asteroidBelts')
        asteroid_belt_fields = self.extract_fields(
            astroid_belts_collection, model_file_name
        )
        self.gen_model_file(model_file_name, asteroid_belt_fields)
        # generate landmark model
        model_file_name = self.convert_to_snake_case('landmarks')
        landmark_fields = self.extract_fields(landmark_collection, model_file_name)
        self.gen_model_file(model_file_name, landmark_fields)

    def gen_model_file(self, model_name, fields):
        context = {
            'model_name': self.convert_to_singular_noun(
                self.convert_to_pascal_case(model_name)
            ),
            'fields': fields,
            'indexes': MODEL_INDEX_RULES.get(model_name, []),
        }

        template = Template(MODEL_TEMPLATE)

        with Path(
            settings.BASE_DIR / 'apps' / 'sde' / 'models' / f'{model_name}.py'
        ).open('w', encoding='utf-8') as f:
            f.write(template.render(Context(context)))

    def gen_model_init(self):
        context = {'models': [], 'imports': []}
        template = Template(INIT_MODEL_TEMPLATE)

        # get all model files in the models directory
        model_files = set(
            Path(settings.BASE_DIR / 'apps' / 'sde' / 'models').glob('*.py')
        )

        for model_file in model_files:
            if model_file.parts[-1] == '__init__.py':
                continue
            file = model_file.parts[-1].replace('.py', '')
            name = self.convert_to_singular_noun(self.convert_to_pascal_case(file))
            context['models'].append(name)
            context['imports'].append(f'from .{file} import {name}')

        with Path(settings.BASE_DIR / 'apps' / 'sde' / 'models' / '__init__.py').open(
            'w', encoding='utf-8'
        ) as f:
            f.write(template.render(Context(context)))

    def gen_universe_lookup_model(self):
        template = Template(UNIVERSE_LOOKUP_TEMPLATE)
        context = {}
        with Path(
            settings.BASE_DIR / 'apps' / 'sde' / 'models' / 'universe_lookup.py'
        ).open('w', encoding='utf-8') as f:
            f.write(template.render(Context(context)))

    def handle(self, *args, **options):
        logger.info('Generating SDE models...')
        logger.info('Collecting all SDE files...')
        self.collect_all_files()
        logger.info('Generating universe models...')
        self.gen_universe_models()
        logger.info('Generating BSD models...')
        self.gen_bsd_models()
        logger.info('Generating FSD models...')
        self.gen_fsd_models()
        logger.info('Generating universe_lookup.py model...')
        self.gen_universe_lookup_model()
        logger.info('Generating __init__.py for models...')
        self.gen_model_init()
        logger.info('SDE model generation complete.')
