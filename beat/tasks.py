from celery import Celery
from celery.schedules import crontab
from pytz import timezone
from apps.task.views import update_installations

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  
    result_serializer='json',
    timezone=timezone("America/Guatemala"),
    enable_utc=False,
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task( crontab(hour=16, minute=5,), get_installations.s())

@app.task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def get_installations():
    update_installations()
    