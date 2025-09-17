#!/bin/bash

set -o errexit
set -o nounset



until timeout 10 celery -A config.celery_app inspect ping; do
    >&2 echo "Celery workers not available"
done

echo 'Starting flower'


watchmedo auto-restart --directory=./apps --directory=./config --pattern=*.py --recursive -- celery -A config.celery_app -b redis://redis:6379 flower --port=5555