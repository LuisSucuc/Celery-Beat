# Run celery

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

# Implementación de celery beat

1. Añadir app a settings
2. Aplicar migraciones

<!--  4. `django-admin startapp app_celery`-->

5. Crear celery.py on app
6. Modificar `__ini__.py` del proyecto principal
7. Añadir lo siguiente a `settings.py`

```python
#Django Celery
CELERY_TIMEZONE = "America/Guatemala"
CELERY_BROKER_URL = 'redis://localhost:6379'
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_TASK_SERIALIZER = 'json'


```

3. `celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
