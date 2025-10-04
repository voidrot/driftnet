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

SDE_CHANGELOG_URL = getattr(
    settings,
    'SDE_CHANGELOG_URL',
    'https://developers.eveonline.com/static-data/tranquility/schema-changelog.yaml',
)

SDE_LATEST_CHANGELOG_VERSION_URL = (
    'https://developers.eveonline.com/static-data/tranquility/latest.jsonl'
)

SDE_LATEST_SDE_EXPORT_URL = 'https://developers.eveonline.com/static-data/eve-online-static-data-latest-jsonl.zip'

SDE_ZIPFILE_DOWNLOAD_NAME = 'sde-export-latest-jsonl.zip'
