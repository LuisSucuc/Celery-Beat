# Run celery

## Celery native

Inicia los procesos con la librería nativa de celery sin implementación de modelos ni basado en base de datos.

Si el archivo de configuración tiene el nombre `celery.py` y el nombre de la aplicación es `beat`

```bash
 celery -A beat worker --loglevel=info
```

Si el archivo de configuración tiene el nombre `tasks.py` y el nombre de la aplicación es `beat`

```bash
 celery -A beat.tasks worker --loglevel=info
```

Iniciar beat nativo de celery

```bash
celery -A beat.tasks beat --loglevel=info
```

## Implementación de celery beat

Se generan los tasks desde la base de datos en donde se define los parámetros y recurrencia de la ejecución.

1. Añadir app a settings `django_celery_beat`
2. Aplicar migraciones de base de datos
3. Crear `celery.py` on app
4. Modificar `__ini__.py` del proyecto principal
5. Iniciar el worker

```bash
celery -A beat worker --loglevel=info
```

6. Iniciar el scheduler que será un listener de la base de datos

```bash
celery -A beat beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

_Las funciones con el decorador `@shared_task` deben encontrarse en el archivo `tasks.py` en cada aplicación._

Si se dea añadir una aplicación de monitorización visual se utiliza debe instalar flower e inicarlo de la siguiente manera:

```bash
flower -A beat --port=5555
```

7. Installar django_celery_results
8. Añadir la aplicación `django_celery_results` en settings
9. Aplicar migraciones
10. aladur la opción `backend='django-db'` al crear la instancia de celery
