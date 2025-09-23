import os

from celery import Celery
from celery.signals import setup_logging

from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('voidlink')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig  # noqa: PLC0415

    dictConfig(settings.LOGGING)


if settings.DEBUG or settings.TEST:
    from celery.signals import task_postrun
    from celery.signals import task_prerun
    from zeal import setup
    from zeal import teardown

    @task_prerun.connect()
    def setup_zeal(*args, **kwargs):
        setup()

    @task_postrun.connect()
    def teardown_zeal(*args, **kwargs):
        teardown()


app.autodiscover_tasks()
