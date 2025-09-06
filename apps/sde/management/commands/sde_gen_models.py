from pathlib import Path
from pprint import pprint
import re
from django.conf import settings
from django.core.management.base import BaseCommand
import logging

import json
from .helpers import collect_files
import inflect

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

logger = logging.getLogger(__name__)
p = inflect.engine()


class Command(BaseCommand):
    help = 'Generate SDE models'

    universe_files = []
    bsd_files = []
    fsd_files = []

    def collect_all_files(self):
        self.universe_files = collect_files(Path(settings.SDE_WORKSPACE / 'universe'))
        self.bsd_files = collect_files(Path(settings.SDE_WORKSPACE / 'bsd'))
        self.fsd_files = collect_files(Path(settings.SDE_WORKSPACE / 'fsd'))

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

    def extract_fields(self, data):
        fields = {}
        field_types = {}
        field_found = {}

        converted_data = []

        if isinstance(data, list):
            converted_data = data

        elif isinstance(data, dict):
            # pass
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
                else:
                    field_found[field_name] += 1
                if type(value).__name__ not in field_types[field_name]:
                    field_types[field_name].append(type(value).__name__)
        pprint('Field types:')
        pprint(field_types)
        # add id field first
        fields['id'] = 'models.IntegerField(primary_key=True)'

        type_map = {
            'int': (
                'models.IntegerField(default=None, null=True)',
                'models.IntegerField()',
            ),
            'float': (
                'models.FloatField(default=None, null=True)',
                'models.FloatField()',
            ),
            'str': ('models.TextField(default=None)', 'models.TextField()'),
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
            # check if we have mizxed types, such as int and float
            # if so we want to choose the higher type
            chosen_type = None
            if len(field_values) > 1:
                if 'float' in field_values:
                    chosen_type = 'float'
                if 'int' in field_values and 'str' in field_values:
                    chosen_type = 'str'
            else:
                chosen_type = field_values[0]

            for py_type, (optional_field, required_field) in type_map.items():
                if py_type == chosen_type:
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
                fields = self.extract_fields(json.load(f))
            self.gen_model_file(model_file_name, fields)

    def gen_bsd_models(self):
        for bsd_file in self.bsd_files:
            fields = {}
            logger.info(f'Processing BSD file: {bsd_file.parts[-1]}')
            model_file_name = self.convert_to_snake_case(
                bsd_file.parts[-1].replace('.json', '')
            )
            with Path(bsd_file).open('r', encoding='utf-8') as f:
                fields = self.extract_fields(json.load(f))
            self.gen_model_file(model_file_name, fields)

    def gen_universe_models(self):
        # TODO: Handle the universe files that are not simple lists of objects or are a single list or object
        for universe_file in self.universe_files:
            fields = {}
            logger.info(f'Processing Universe file: {universe_file}')
            model_file_name = self.convert_to_snake_case(
                universe_file.parts[-1].replace('.json', '')
            )
            with Path(universe_file).open('r', encoding='utf-8') as f:
                fields = self.extract_fields(json.load(f))
            self.gen_model_file(model_file_name, fields)

    def gen_model_file(self, model_name, fields):
        lines = []

        lines.append('from django.db import models')
        lines.append('')
        lines.append('')
        lines.append(
            f'class {self.convert_to_singular_noun(self.convert_to_pascal_case(model_name))}(models.Model):'
        )
        for field_name, field_type in fields.items():
            lines.append(f'    {field_name} = {field_type}')
        lines.append('')
        lines.append('    def __str__(self):')
        if 'name_id' in fields:
            lines.append(f'        return f\'{{self.name_id["en"]}}\'')
        else:
            lines.append(f"        return f'{{self.id}}'")

        # end of file
        lines.append('')

        with Path(
            settings.BASE_DIR / 'apps' / 'sde' / 'models' / f'{model_name}.py'
        ).open('w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

        # print('\n'.join(lines))

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
