from celery import Celery
from pytz import timezone
import logging


app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')

app.conf.update(
    task_serializer='json',
    #accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone=timezone("America/Guatemala"),
    #enable_utc=True,
)
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    
    # Calls test('hello') every 10 seconds.
    #sender.add_periodic_task(10.0, test.s('hello 10 seconds'), name='add every 10')

    # Calls test('world') every 30 seconds
    #sender.add_periodic_task(30.0, test.s('hello 30 seconds'), expires=10)
    sender.add_periodic_task(5.0, test.s('5 seconds'))

    # Executes every Monday morning at 7:30 a.m.
    #sender.add_periodic_task(
    #    crontab(hour=7, minute=30, day_of_week=1),
    #    test.s('Happy Mondays!'),
    #)

@app.task
def test(arg):
    logging.info(arg)
    print(arg)
    return arg