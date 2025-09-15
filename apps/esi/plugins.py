from aiopenapi3.plugin import Document


class RemoveSecurityParameter(Document):
    """
    Removes the whole OAuth2 securityScheme
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


class PatchCompatibilityDatePlugin(Document):
    """
    Makes the X-Compatibility-Date header optional

    This is because WE specifically add it in the library to the HTTP requests,
    but without this, it will be a required parameter during request generation before it hits the HTTP library.
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
