# Register your models here.
import contextlib

from django.apps import apps
from django.contrib import admin


# Programmatically register simple ModelAdmin classes for all models in this app
def _get_field_names(model, limit=4):
    """Return up to `limit` field names for use in list_display."""
    # Prefer non-auto fields and non-relational fields for simple display
    names = [
        f.name
        for f in model._meta.get_fields()
        if getattr(f, 'concrete', False) and not f.many_to_many and not f.one_to_many
    ]
    # If no fields found (unlikely), fall back to PK name
    if not names:
        return [model._meta.pk.name]
    return names[:limit]


for model in apps.get_app_config('sde').get_models():
    admin_class = type(
        f'{model.__name__}Admin',
        (admin.ModelAdmin,),
        {
            'list_display': [
                f.name
                for f in model._meta.get_fields()
                if getattr(f, 'concrete', False)
            ],
            'search_fields': [
                f.name
                for f in model._meta.get_fields()
                if f.name.endswith('_id') or f.name == 'name'
            ],
        },
    )
    with contextlib.suppress(admin.sites.AlreadyRegistered):  # mypy: ignore
        admin.site.register(model, admin_class)
