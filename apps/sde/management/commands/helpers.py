from pathlib import Path


def collect_files(collection_dir: Path):
    return [
        entry
        for entry in collection_dir.rglob('**')
        if entry.is_file() and entry.suffix in ['.json']
    ]
