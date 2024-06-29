from celery import Celery
import time
from django.core.management.base import BaseCommand
from myapp.cron import my_scheduled_job
from celery import shared_task
import time
import unittest

app = celery_app



class Command(BaseCommand):
    help = 'Runs a task every 3 minutes 40 seconds'

    def handle(self, *args, **options):
        while True:
            my_scheduled_job()  # Call the scheduled job correctly
            time.sleep(220)


@shared_task
def task_every_220_seconds():
    print("Task runs every 3 minutes 40 seconds")

@shared_task
def task_three_times_evening():
    print("Task runs 3 times in the evening")

@app.task(bind=True, ignore_result=True)  # Corrected the parameter spelling
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def add(x, y):
    return x + y