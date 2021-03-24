# Run celery

Si el archivo de configuración tiene el nombre `celery.py` y el nombre de la aplicación es `beat`

```bash
 celery -A beat worker --loglevel=info
```

Si el archivo de configuración tiene el nombre `tasks.py` y el nombre de la aplicación es `beat`

```bash
 celery -A beat.tasks worker --loglevel=info
```