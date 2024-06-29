from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django .conf import settings
import importlib
import import_module


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bernikovich_Django1.settings')


app = Celery('Bernikovich_Django1')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

def create_celery_app():
    from celery import Celery
    Celery('my_app')
    return app


def create_celery_app():
    from celery import Celery
    Celery('my_app')

    app.conf.update(
        broker_url='redis://localhost:6379/0',
        result_backend='redis://localhost:6379/0',
        # Add any other configuration settings here
    )
    return app

if __name__ == '__main__':
    celery_app = create_celery_app()
@app.task()
def import_module_task():
    importlib.import_module('celery.some submodule')


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')