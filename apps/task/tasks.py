from celery import shared_task


@shared_task
def update_installations_shared():
    import requests
    req = requests.get('https://jsonplaceholder.typicode.com/todos')
    print(req)
    #print(req.text)
    print("Actualización finalizada con ÉXITO")


