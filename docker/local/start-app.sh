#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py migrate

exec uvicorn config.asgi:application --host 0.0.0.0 --reload --reload-include '*.html'