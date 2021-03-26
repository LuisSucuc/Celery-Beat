import os

from celery import Celery
from pytz import timezone

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beat.settings')

app = Celery('proj', broker='redis://localhost:6379', backend='redis://localhost:6379')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  
    result_serializer='json',
    timezone=timezone("America/Guatemala"),
    enable_utc=False,
)


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')