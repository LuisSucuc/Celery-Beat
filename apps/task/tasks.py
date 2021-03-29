from celery import shared_task
from datetime import datetime


@shared_task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 20})
def update_installations_shared(self):
    #raise Exception("asadfasdfsafasdfasdfasdfasdf")
    import requests
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    #print(req)
    txt = f"Actualización finalizada con ÉXITO {str(datetime.now())}"
    print(txt)
    return txt


