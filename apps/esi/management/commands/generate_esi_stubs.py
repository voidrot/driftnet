import contextlib
import os
import re

from django.core.management.base import BaseCommand

from apps.esi import client_stubs
from apps.esi.client import ESIClientProvider

# OpenAPI Types to Python
TYPE_MAP = {
    'integer': 'int',
    'number': 'float',
    'string': 'str',
    'boolean': 'bool',
    'array': 'list[Any]',
    'object': 'dict[str, Any]',
}


def sanitize_class_name(name: str) -> str:
    """Convert a tag into a valid Python class name."""
    sanitized = re.sub(r'[^0-9a-zA-Z_]', '_', name.strip())
    if sanitized and not sanitized[0].isalpha():
        sanitized = f'_{sanitized}'
    return sanitized


def sanitize_operation_class(name: str) -> str:
    return re.sub(r'[^0-9a-zA-Z_]', '', name[0].upper() + name[1:] + 'Operation')


def schema_to_type(schema, models: dict) -> str:
    """Convert an OpenAPI schema to a Python type hint or Pydantic model, recursively collecting referenced schemas."""
    if not schema:
        return 'Any'
    schema_type = getattr(schema, 'type', None)
    # Handle case where type is a list (e.g. ["string", "null"])
    if isinstance(schema_type, list):
        # Prefer first non-null type, fallback to 'Any'
        non_null_types = [t for t in schema_type if t != 'null']
        schema_type = non_null_types[0] if non_null_types else 'Any'
    if schema_type == 'array':
        items_schema = getattr(schema, 'items', None)
        inner = schema_to_type(items_schema, models)
        return f'List[{inner}]'
    if schema_type == 'object':
        ref = getattr(schema, 'ref', None)
        if ref:
            model_name = ref.split('/')[-1]
            if model_name not in models:
                models[model_name] = schema
                # Recursively collect properties of referenced schema
                props = getattr(schema, 'properties', {})
                for prop_schema in props.values():
                    schema_to_type(prop_schema, models)
            return model_name
        name = getattr(schema, 'title', None) or 'InlineModel'
        model_name = sanitize_class_name(name)
        if model_name not in models:
            models[model_name] = schema
            # Recursively collect properties of inline object schema
            props = getattr(schema, 'properties', {})
            for prop_schema in props.values():
                schema_to_type(prop_schema, models)
        return model_name
    # If schema has properties but no explicit type, treat as object
    if hasattr(schema, 'properties') and getattr(schema, 'properties', None):
        name = getattr(schema, 'title', None) or 'InlineModel'
        model_name = sanitize_class_name(name)
        if model_name not in models:
            models[model_name] = schema
            props = getattr(schema, 'properties', {})
            for prop_schema in props.values():
                schema_to_type(prop_schema, models)
        return model_name
    key = schema_type if isinstance(schema_type, str) else 'Any'
    return TYPE_MAP.get(key, 'Any')


class Command(BaseCommand):
    help = 'Generate ESI Stubs from the current ESI spec with correct type hints.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            default=None,
            help='Custom output path for the generated ESI stub file (default: client_stubs.pyi next to openapi_clients.py).',
        )

    def handle(self, *args, **options):
        self.stdout.write('Starting ESI stub generation...')

        stub_api = ESIClientProvider()
        stub_api = stub_api.client.api
        base_path = os.path.dirname(client_stubs.__file__)
        output_path = options['output'] or os.path.join(base_path, 'client_stubs.pyi')
        self.stdout.write(f'Outputting to: {output_path}')
        spec_root = stub_api._root
        with open(output_path, 'w', encoding='utf-8') as f:
            # File headers
            f.write('# ruff: noqa\n')
            f.write('# Auto Generated do not edit\n')
            # Python Imports
            models = {}
            operation_classes = {}

            # First pass: collect all schemas for response/request bodies
            for tag in sorted(stub_api._operationindex._tags.keys()):
                ops = stub_api._operationindex._tags[tag]
                for nm, op in sorted(ops._operations.items()):
                    op_type = op[0]
                    op_obj = op[2]
                    try:
                        match op_type:
                            case 'post':
                                resp_201 = op_obj.responses.get('201')
                                if resp_201 and 'application/json' in resp_201.content:
                                    schema_to_type(
                                        resp_201.content['application/json'].schema_,
                                        models,
                                    )
                            case 'put' | 'delete':
                                pass
                            case _:
                                resp_200 = op_obj.responses.get('200')
                                if resp_200 and 'application/json' in resp_200.content:
                                    schema_to_type(
                                        resp_200.content['application/json'].schema_,
                                        models,
                                    )
                    except Exception:  # noqa: S110
                        pass
                    if getattr(op_obj, 'requestBody', None):
                        with contextlib.suppress(Exception):
                            schema_to_type(
                                op_obj.requestBody.content['application/json'].schema_,
                                models,
                            )

            # Scan models for alias usage
            for model_name, schema in list(models.items()):
                props = getattr(schema, 'properties', {})
                for prop, prop_schema in props.items():
                    alias = getattr(prop_schema, 'x-python-alias', None)
                    if alias:
                        break

            f.write('from typing import Any, List, Optional\n')
            f.write('from pydantic import BaseModel, Field\n')
            f.write('from apps.esi.client import ESIClientOperation\n')
            f.write('from apps.esi.models import Token\n\n\n')

            # Generate Pydantic models
            for model_name, schema in list(models.items()):
                f.write(f'class {model_name}(BaseModel):\n')
                props = getattr(schema, 'properties', {})
                required = set(getattr(schema, 'required', []))
                if not props:
                    f.write('    pass\n\n')
                    continue
                for prop, prop_schema in props.items():
                    typ = schema_to_type(prop_schema, models)
                    is_required = prop in required
                    # Check for alias in extensions['python-alias'] or x-python-alias
                    alias = None
                    if hasattr(prop_schema, 'extensions') and prop_schema.extensions:
                        alias = prop_schema.extensions.get('python-alias')
                    if not alias:
                        alias = getattr(prop_schema, 'x-python-alias', None)
                    # is_list = typ.startswith('List[')
                    # Fix: Use Optional[List[...]] for optional list fields
                    # if not is_required and is_list:
                    if not is_required:
                        typ = f'Optional[{typ}]'
                    if alias:
                        field_str = (
                            f"Field(..., alias='{alias}')"
                            if is_required
                            else f"Field(None, alias='{alias}')"
                        )
                        f.write(f'    {prop}: {typ} = {field_str}\n')
                    else:
                        default = '' if is_required else ' = None'
                        f.write(f'    {prop}: {typ}{default}\n')
                f.write('\n')

            # Generate operation classes
            for tag in sorted(stub_api._operationindex._tags.keys()):
                ops = stub_api._operationindex._tags[tag]
                for nm, op in sorted(ops._operations.items()):
                    op_type = op[0]
                    op_obj = op[2]
                    docstring = (
                        (op_obj.description or op_obj.summary or '')
                        .replace('\n', ' ')
                        .strip()
                    )
                    op_class_name = sanitize_operation_class(nm)

                    response_type = 'Any'
                    try:
                        match op_type:
                            case 'post':
                                resp_201 = op_obj.responses.get('201')
                                if resp_201 and 'application/json' in resp_201.content:
                                    response_type = schema_to_type(
                                        resp_201.content['application/json'].schema_,
                                        models,
                                    )
                            case 'put' | 'delete':
                                response_type = 'None'
                            case _:
                                resp_200 = op_obj.responses.get('200')
                                if resp_200 and 'application/json' in resp_200.content:
                                    response_type = schema_to_type(
                                        resp_200.content['application/json'].schema_,
                                        models,
                                    )
                    except Exception:
                        response_type = 'Any'

                    results_type = (
                        response_type
                        if str(response_type).startswith('List[')
                        else f'List[{response_type}]'
                    )

                    if op_class_name not in operation_classes:
                        f.write(f'class {op_class_name}(ESIClientOperation):\n')
                        if response_type != 'None':
                            f.write(
                                '    """ESIClientOperation, use result(), results() or results_localized()"""\n'
                            )
                        else:
                            f.write('    """ESIClientOperation, use result()"""\n')

                        # result()
                        f.write(
                            f'    def result(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> {response_type}:\n'
                        )
                        f.write(f'        """{docstring}"""\n') if docstring else None
                        f.write('        ...\n\n')
                        if response_type != 'None':
                            f.write(
                                f'    def results(self, use_etag: bool = True, return_response: bool = False, force_refresh: bool = False, use_cache: bool = True, **extra) -> {results_type}:\n'
                            )
                            f.write(
                                f'        """{docstring}"""\n'
                            ) if docstring else None
                            f.write('        ...\n\n')

                            f.write(
                                f'    def results_localized(self, languages: List[str] | str | None = None, **extra) -> dict[str, {results_type}]:\n'
                            )
                            f.write(
                                f'        """{docstring}"""\n'
                            ) if docstring else None
                            f.write('        ...\n\n\n')

                        operation_classes[op_class_name] = True

            # Generate ESIClientStub
            f.write('class ESIClientStub:\n')
            for tag in sorted(stub_api._operationindex._tags.keys()):
                ops = stub_api._operationindex._tags[tag]
                class_name = f'_{sanitize_class_name(tag)}'
                f.write(f'    class {class_name}:\n')
                for nm, op in sorted(ops._operations.items()):
                    op_obj = op[2]
                    effective_security = getattr(op_obj, 'security', None) or getattr(
                        spec_root, 'security', None
                    )

                    def _has_oauth2(sec) -> bool:
                        data = (
                            sec if isinstance(sec, dict) else getattr(sec, 'root', None)
                        )
                        if not isinstance(data, dict):
                            return False
                        return any(k.lower() == 'oauth2' for k in data)

                    needs_oauth = any(
                        _has_oauth2(s) for s in (effective_security or [])
                    )

                    params = ['self']
                    optional_params = []
                    if getattr(op_obj, 'requestBody', None):
                        params.append(
                            f'body: {schema_to_type(op_obj.requestBody.content["application/json"].schema_, models)}'
                        )

                    for p in getattr(op_obj, 'parameters', []):
                        required = getattr(p, 'required', False)
                        schema_type_value = getattr(
                            getattr(p, 'schema_', None), 'type', None
                        )
                        if isinstance(schema_type_value, str):
                            param_type = TYPE_MAP.get(schema_type_value, 'Any')
                        else:
                            param_type = 'Any'
                        default = ''
                        if not required:
                            param_type = f'Optional[{param_type}]'
                            default = ' = ...'
                        param_name = p.name.replace('-', '_')
                        if param_name == 'authorization' and needs_oauth:
                            continue
                        if required:
                            params.append(f'{param_name}: {param_type}{default}')
                        else:
                            optional_params.append(
                                f'{param_name}: {param_type}{default}'
                            )
                    if needs_oauth:
                        params.append('token: Token')
                    optional_params.append('**kwargs: Any')
                    params_str = ', '.join(params + optional_params)
                    op_class_name = sanitize_operation_class(nm)
                    docstring = (
                        (op_obj.description or op_obj.summary or '')
                        .replace('\n', ' ')
                        .strip()
                    )

                    if docstring:
                        f.write(f'        def {nm}({params_str}) -> {op_class_name}:\n')
                        f.write(f'            """{docstring}"""\n')
                        f.write('            ...\n\n')
                    else:
                        f.write(
                            f'        def {nm}({params_str}) -> {op_class_name}: ...\n'
                        )
                f.write(
                    f'\n    {sanitize_class_name(tag)}: {class_name} = {class_name}()\n\n'
                )

        self.stdout.write(self.style.SUCCESS(f'ESI stubs written to {output_path}'))
