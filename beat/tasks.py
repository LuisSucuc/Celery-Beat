from celery import Celery
from celery.schedules import crontab
from pytz import timezone
from datetime import datetime

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
    #sender.add_periodic_task(5.0, test.s('hello'), name='add every 10')

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task( crontab(hour=15, minute=41,), test.s('Happy Mondays 0!'),)

@app.task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2})
def test(arg):
    print("\n\n\n\n")
    raise Exception('--------> ERROR <-------------')
    