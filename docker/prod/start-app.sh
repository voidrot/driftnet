#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

python /app/manage.py collectstatic --noinput

exec gunicorn config.asgi --bind 0.0.0.0:8000 --chdir=/app -k uvicorn_worker.UvicornWorker