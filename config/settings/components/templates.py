from config.settings.components.common import APPS_DIR

# Gather all app template directories

APP_TEMPLATE_DIRS = [
    str(app_dir / 'templates')
    for app_dir in APPS_DIR.iterdir()
    if (app_dir / 'templates').is_dir() and (app_dir / 'app.py').is_file()
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'loaders': [
            #     (
            #         'template_partials.loader.Loader',
            #         [
            #             (
            #                 'django.template.loaders.cached.Loader',
            #                 [
            #                     'django_cotton.cotton_loader.Loader',
            #                     'django.template.loaders.filesystem.Loader',
            #                     'django.template.loaders.app_directories.Loader',
            #                 ],
            #             )
            #         ],
            #     ),
            # ],
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django_cotton.templatetags.cotton',
            ],
        },
    },
]
