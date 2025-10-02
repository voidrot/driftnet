import logging
import re
from pathlib import Path
from typing import Literal

import inflect
import jsonlines
import textcase
from django.conf import settings
from django.core.management.base import BaseCommand
from django.template import Context
from django.template import Template

from apps.sde import app_settings
from apps.sde.management.commands.helpers import INIT_MODEL_TEMPLATE
from apps.sde.management.commands.helpers import MODEL_FOREIGN_KEY_OVERRIDE
from apps.sde.management.commands.helpers import MODEL_INDEX_RULES
from apps.sde.management.commands.helpers import MODEL_TEMPLATE

logger = logging.getLogger(__name__)
p = inflect.engine()

COLUMN_TYPE_MAP = {
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

PG_INT_MIN = -2147483648
PG_INT_MAX = 2147483647

IGNORED_FILES = ['_sde.jsonl', 'translationLanguages.jsonl']

IGNORED_CONVERT_TO_SINGULAR = [
    'typeBonus.jsonl',
    'typeDogma.jsonl',
    'agentsInSpace.jsonl',
    'types.jsonl',
]


class Command(BaseCommand):
    help = 'Generate SDE models'

    workspace_dir = Path(app_settings.SDE_WORKSPACE)
    extracted_dir = workspace_dir / 'extracted'
    model_context = []

    def collect_files(self):
        """Recursively collect all .json files in the extracted directory."""
        self.target_files = [
            entry
            for entry in self.extracted_dir.rglob('*')
            if entry.is_file()
            and entry.suffix in ['.jsonl']
            and entry.name not in IGNORED_FILES
        ]

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

    def convert_to_singular_noun(self, name):
        """Convert a string to singular noun."""
        word = p.singular_noun(name)
        if not word:
            logger.warning(f'Failed to convert {name} to singular noun.')
            return name
        return word

    def extract_fields_and_types(self):
        column_types: dict[
            str, dict[str, str]
        ] = {}  # model_name -> field_name -> field_type
        field_found: dict[str, dict[str, int]] = {}  # model_name -> field_name -> count
        field_count: dict[str, int] = {}  # model_name -> total_count

        def get_field_type(
            value,
        ) -> Literal['int', 'bigint', 'float', 'str', 'bool', 'list', 'dict'] | None:
            # Map Python types to field types
            if isinstance(value, int):
                return 'int' if PG_INT_MIN <= value <= PG_INT_MAX else 'bigint'
            if isinstance(value, float):
                return 'float'
            if isinstance(value, str):
                return 'str'
            if isinstance(value, bool):
                return 'bool'
            if isinstance(value, list):
                return 'list'
            if isinstance(value, dict):
                return 'dict'
            return None

        for file in self.target_files:
            model_file_name = textcase.snake(
                self.convert_to_singular_noun(file.stem)
                if file.name not in IGNORED_CONVERT_TO_SINGULAR
                else file.stem
            )
            model_name = textcase.pascal(
                self.convert_to_singular_noun(file.stem)
                if file.name not in IGNORED_CONVERT_TO_SINGULAR
                else file.stem
            )
            logger.info(
                f'Processing file: {file.name}, File Name: {model_file_name}, Model: {model_name}'
            )
            column_types.setdefault(model_name, {})
            field_found.setdefault(model_name, {})
            field_count.setdefault(model_name, 0)
            with jsonlines.open(file) as reader:
                for obj in reader:
                    field_count[model_name] += 1
                    for key, value in obj.items():
                        if key not in field_found[model_name]:
                            field_found[model_name][key] = 0
                        field_found[model_name][key] += 1
                        if key not in column_types[model_name]:
                            field_type = get_field_type(value)
                            if field_type:
                                column_types[model_name][key] = field_type
                            else:
                                logger.warning(
                                    f'Unknown type for key {key}: {type(value)}'
                                )
        logger.info('Completed processing all files.')

        # Determine final field types with nullability
        final_column_types: dict[str, dict[str, str]] = {}
        for model, fields in column_types.items():
            final_column_types[model] = {}
            for field in fields:
                field_type = fields[field]
                if field_found[model][field] < field_count[model]:
                    final_column_types[model][field] = COLUMN_TYPE_MAP[field_type][
                        0
                    ]  # nullable
                else:
                    final_column_types[model][field] = COLUMN_TYPE_MAP[field_type][
                        1
                    ]  # non-nullable

        self.model_columns = final_column_types

    def modify_model_context_with_rules(
        self, model_name: str, columns: dict[str, str]
    ) -> dict[str, str]:
        context = {
            'model_file_name': textcase.snake(model_name),
            'model_name': model_name,
            'fields': [],
            'indexes': [],
            'imports': [],
            'verbose_name': textcase.title(model_name) or model_name,
            'verbose_name_plural': p.plural_noun(textcase.title(model_name))
            or textcase.title(model_name),
        }
        foreign_key_update = MODEL_FOREIGN_KEY_OVERRIDE.get(
            context['model_file_name'], None
        )

        for field, _type in columns.items():
            field_name = 'id' if field == '_key' else self.convert_to_snake_case(field)
            if field_name == 'id':
                field_split = _type.split('(')
                field_type = field_split[0] + '(primary_key=True' + field_split[1]
            elif foreign_key_update and field_name in foreign_key_update:
                field_type = foreign_key_update[field_name]['field']
                context['imports'].append(foreign_key_update[field_name]['import'])
            else:
                field_type = _type
            context['fields'].append(
                {
                    'name': field_name,
                    'type': field_type,
                }
            )

        if context['model_file_name'] in MODEL_INDEX_RULES:
            context['indexes'].extend(MODEL_INDEX_RULES[context['model_file_name']])

        return context

    def gen_model_files(self):
        template = Template(MODEL_TEMPLATE)
        for model, columns in self.model_columns.items():
            context = Context(self.modify_model_context_with_rules(model, columns))
            with (
                Path(settings.BASE_DIR)
                / 'apps'
                / 'sde'
                / 'models'
                / f'{context["model_file_name"]}.py'
            ).open('w', encoding='utf-8') as f:
                f.write(template.render(context))

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
            name = textcase.pascal(file)
            context['models'].append(name)
            context['imports'].append(f'from .{file} import {name}')

        with Path(settings.BASE_DIR / 'apps' / 'sde' / 'models' / '__init__.py').open(
            'w', encoding='utf-8'
        ) as f:
            f.write(template.render(Context(context)))

    def handle(self, *args, **options):
        logger.info('Generating SDE models...')
        logger.info('Collecting all SDE files...')
        self.collect_files()
        self.extract_fields_and_types()
        self.gen_model_files()
        self.gen_model_init()
        logger.info('SDE model generation complete.')
