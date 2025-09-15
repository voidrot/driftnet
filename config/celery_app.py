import os

from celery import Celery
from celery.signals import setup_logging
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('voidlink')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Configure separate queues so we can use rate limiting to avoid
# hitting API limits.
# app.conf.task_queues = {
#     Queue('default', Exchange('default'), routing_key='default'),
#     Queue('esi', Exchange('esi'), routing_key='esi'),
# }

# app.conf.task_default_queue = 'default'
# app.conf.task_default_exchange_type = 'direct'
# app.conf.task_default_routing_key = 'default' # pyright: ignore[reportAttributeAccessIssue]


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig  # noqa: PLC0415

    dictConfig(settings.LOGGING)


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
