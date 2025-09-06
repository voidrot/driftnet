#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# convert-sde-yaml-to-json.sh
# Recursively convert all .yml/.yaml files under the given directory
# to JSON files next to the original files using mikefarah's `yq`.
#
# Usage:
#   ./scripts/convert-sde-yaml-to-json.sh [ROOT_DIR]
#
# If ROOT_DIR is omitted the script will use `.sde_workspace`.

ROOT_DIR="${1:-.sde_workspace}"

if ! command -v yq >/dev/null 2>&1; then
  echo "Error: yq not found. Install mikefarah/yq (https://github.com/mikefarah/yq) and ensure 'yq' is on PATH." >&2
  exit 2
fi

if [ ! -d "$ROOT_DIR" ]; then
  echo "Error: directory '$ROOT_DIR' does not exist." >&2
  exit 3
fi

echo "Converting YAML files under: $ROOT_DIR"

# Find YAML files and convert them. Use -print0 to support spaces/newlines in names.
find "$ROOT_DIR" -type f \( -iname '*.yml' -o -iname '*.yaml' \) -print0 |
while IFS= read -r -d '' file; do
  dest="${file%.*}.json"
  mkdir -p "$(dirname "$dest")"
  printf 'Converting: %s -> %s\n' "$file" "$dest"

  # Use yq v4: eval with -o=json to produce JSON output
  if ! yq eval -o=json '.' "$file" > "$dest"; then
    echo "Error: failed to convert $file" >&2
    exit 4
  fi
done

echo "All conversions complete."
