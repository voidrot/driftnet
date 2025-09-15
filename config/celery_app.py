import os

from celery import Celery
from celery.signals import setup_logging
from django.conf import settings
from kombu import Exchange
from kombu import Queue

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('voidlink')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


# Configure multiple queues and exchanges
app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('esi', Exchange('esi'), routing_key='esi'),
    Queue(
        'esi_server_status',
        Exchange('esi_server_status'),
        routing_key='esi_server_status',
    ),
    Queue('esi_wars', Exchange('esi_wars'), routing_key='esi_wars'),
)

app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'default'

app.conf.task_routes = {
    'apps.esi.tasks.*': {'queue': 'esi', 'exchange': 'esi', 'routing_key': 'esi'},
    'apps.server_status.tasks.*': {
        'queue': 'esi_server_status',
        'exchange': 'esi_server_status',
        'routing_key': 'esi_server_status',
    },
    'apps.wars.tasks.*': {
        'queue': 'esi_wars',
        'exchange': 'esi_wars',
        'routing_key': 'esi_wars',
    },
}


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig  # noqa: PLC0415

    dictConfig(settings.LOGGING)


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
