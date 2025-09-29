import keyword

from aiopenapi3.plugin import Document


class Trim204ContentType(Document):
    """
    Plugin for aiopenapi3 that removes the 'content' field from 204 responses in OpenAPI specs.

    Why:
        According to HTTP standards, a 204 No Content response must not include a response body,
        and therefore should not specify a content-type. Some OpenAPI specs incorrectly include
        a content-type for 204 responses, which can cause issues with code generation and validation.
        This plugin ensures that 204 responses do not specify a content-type, improving spec compliance.

    Usage:
        Register this plugin with aiopenapi3 to automatically patch OpenAPI documents after parsing.
    """

    def parsed(self, ctx: Document.Context) -> Document.Context:
        spec = ctx.document
        # Patch all paths
        for path_item in spec.get('paths', {}).values():
            for method_name in (
                'get',
                'post',
                'put',
                'delete',
                'patch',
                'options',
                'head',
            ):
                method = path_item.get(method_name)
                if not method:
                    continue
                if '204' in method['responses']:
                    method['responses']['204'].pop('content', [])
        return ctx


class Add304ContentType(Document):
    """
    Plugin for aiopenapi3 that ensures OpenAPI specs include a 304 response without a content-type.

    Why:
        According to HTTP standards, a 304 Not Modified response must not include a response body,
        and therefore should not specify a content-type. Some OpenAPI specs incorrectly omit the 304 response,
        or include a content-type, which can cause issues with code generation and validation.
        This plugin adds a minimal 304 response entry with only a description, ensuring spec compliance.

    Usage:
        Register this plugin with aiopenapi3 to automatically patch OpenAPI documents after parsing.
    """

    def parsed(self, ctx: Document.Context) -> Document.Context:
        spec = ctx.document
        # Patch all paths
        for path_item in spec.get('paths', {}).values():
            for method_name in (
                'get',
                'post',
                'put',
                'delete',
                'patch',
                'options',
                'head',
            ):
                method = path_item.get(method_name)
                if not method:
                    continue
                if '304' not in method['responses']:
                    method['responses']['304'] = {'description': 'Not Modified'}
        return ctx


class RemoveSecurityParameter(Document):
    """
    Plugin for aiopenapi3 that removes the OAuth2 security scheme and all security requirements from OpenAPI specs.

    Why:
        Some OpenAPI specifications include OAuth2 security schemes and security requirements that may not be needed
        or may interfere with client code generation and authentication flows. This plugin removes the OAuth2
        security scheme from the 'components.securitySchemes' section and strips all 'security' requirements from
        each operation in the spec, simplifying the document for use cases where authentication is handled externally.

    Usage:
        Register this plugin with aiopenapi3 to automatically patch OpenAPI documents after parsing.
    """

    def parsed(self, ctx: Document.Context) -> Document.Context:
        spec = ctx.document
        spec.get('components', {}).get('securitySchemes', {}).pop('OAuth2', None)
        # Patch all paths
        for path_item in spec.get('paths', {}).values():
            for method_name in (
                'get',
                'post',
                'put',
                'delete',
                'patch',
                'options',
                'head',
            ):
                method = path_item.get(method_name)
                if not method:
                    continue
                method.pop('security', None)

        return ctx


class TrimSecurityParameter(Document):
    """
    Plugin for aiopenapi3 that trims out-of-spec OAuth2 attributes from OpenAPI specs.

    Why:
        Some OpenAPI specifications may include non-standard OAuth2 attributes such as 'in' and 'name'.
        These attributes are not part of the official OAuth2 security scheme definition and can cause
        compatibility issues with tools that strictly validate OpenAPI documents. This plugin removes
        these attributes from the OAuth2 security scheme if present.

    Usage:
        Register this plugin with aiopenapi3 to automatically patch OpenAPI documents after parsing.
        This is mainly kept for quick reference in case similar issues arise again.
    """

    def parsed(self, ctx: Document.Context) -> Document.Context:
        spec = ctx.document
        oauth2 = spec.get('components', {}).get('securitySchemes', {}).get('OAuth2')
        if oauth2 and oauth2.get('type') == 'oauth2':
            oauth2.pop('in', None)
            oauth2.pop('name', None)
        return ctx


class PrefixReservedKeywords(Document):
    """
    Plugin for aiopenapi3 that prefixes reserved Python keywords in schema properties with '_' and sets x-python-alias for code generation.

    Why:
        OpenAPI schemas may use property names that are reserved Python keywords (e.g., 'from', 'class', 'def'), which causes syntax errors in generated models.
        This plugin renames such properties by prefixing them with '_', and sets an 'x-python-alias' extension for code generators to use the alias for the Python attribute name.

    Usage:
        Register this plugin with aiopenapi3 to automatically patch OpenAPI documents after parsing.
    """

    def parsed(self, ctx: Document.Context) -> Document.Context:
        spec = ctx.document
        schemas = spec.get('components', {}).get('schemas', {})
        for schema in schemas.values():
            properties = schema.get('properties', {})
            reserved = [p for p in properties if keyword.iskeyword(p)]
            for prop_name in reserved:
                new_name = '_' + prop_name
                properties[new_name] = properties.pop(prop_name)
                properties[new_name]['x-python-alias'] = prop_name
                if 'required' in schema and prop_name in schema['required']:
                    schema['required'].remove(prop_name)
                    schema['required'].append(new_name)
        return ctx


class PatchCompatibilityDatePlugin(Document):
    """
    Plugin for aiopenapi3 that makes the 'X-Compatibility-Date' header optional in OpenAPI specs.

    Why:
        Some OpenAPI specifications mark the 'X-Compatibility-Date' header as required, which can force client code
        to provide it before sending requests. In cases where the library itself adds this header automatically,
        it should not be required at the OpenAPI spec level. This plugin patches both inline and referenced
        'X-Compatibility-Date' header parameters to set 'required' to False, ensuring smoother client code generation.

    Usage:
        Register this plugin with aiopenapi3 to automatically patch OpenAPI documents after parsing.
    """

    def parsed(self, ctx: Document.Context) -> Document.Context:
        spec = ctx.document

        def patch_param(param):
            # Follow $ref if present
            if '$ref' in param:
                ref = param['$ref']
                parts = ref.split('/')
                if parts[1] == 'components' and parts[2] == 'parameters':
                    param_name = parts[-1]
                    comp_param = (
                        spec.get('components', {}).get('parameters', {}).get(param_name)
                    )
                    if comp_param and comp_param.get('name') == 'X-Compatibility-Date':
                        comp_param['required'] = False
            # Inline parameter
            elif (
                param.get('name') == 'X-Compatibility-Date'
                and param.get('in') == 'header'
            ):
                param['required'] = False

        # Patch all paths
        for path_item in spec.get('paths', {}).values():
            for method_name in (
                'get',
                'post',
                'put',
                'delete',
                'patch',
                'options',
                'head',
            ):
                method = path_item.get(method_name)
                if not method:
                    continue
                for param in method.get('parameters', []):
                    patch_param(param)

        # Patch global parameters in components
        for param in spec.get('components', {}).get('parameters', {}).values():
            if (
                param.get('name') == 'X-Compatibility-Date'
                and param.get('in') == 'header'
            ):
                param['required'] = False

        return ctx
