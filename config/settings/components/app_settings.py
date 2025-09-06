from pathlib import Path

from config.env import BASE_DIR

# SDE
SDE_WORKSPACE = Path(BASE_DIR / '.sde_workspace')
SDE_ARCHIVE_URL = (
    'https://eve-static-data-export.s3-eu-west-1.amazonaws.com/tranquility/sde.zip'
)
SDE_CHECKSUM_URL = (
    'https://eve-static-data-export.s3-eu-west-1.amazonaws.com/tranquility/checksum'
)
SDE_CHECKSUM_FILE = SDE_WORKSPACE / 'checksum'
SDE_HOBOLEAKS_BASE_URL = 'https://sde.hoboleaks.space/tq/'
