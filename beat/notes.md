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
5. Iniciar el worker `celery -A beat worker --loglevel=info`
6. Iniciar el scheduler que será un listener de la base de datos `celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`

_Las funciones con el decorador `@shared_task` deben encontrarse en el archivo `tasks.py` en cada aplicación._
