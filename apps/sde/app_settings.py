from pathlib import Path

from django.conf import settings

SDE_WORKSPACE = getattr(
    settings, 'SDE_WORKSPACE', Path(settings.BASE_DIR / '.sde_workspace')
)
SDE_CHECKSUM_URL = getattr(
    settings,
    'SDE_CHECKSUM_URL',
    'https://eve-static-data-export.s3-eu-west-1.amazonaws.com/tranquility/checksum',
)
SDE_ARCHIVE_URL = getattr(
    settings,
    'SDE_ARCHIVE_URL',
    'https://eve-static-data-export.s3-eu-west-1.amazonaws.com/tranquility/sde.zip',
)

SDE_CHECKSUM_FILE = SDE_WORKSPACE / 'checksum'

SDE_HOBOLEAKS_BASE_URL = 'https://sde.hoboleaks.space/tq/'
