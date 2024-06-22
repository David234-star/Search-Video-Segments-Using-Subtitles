from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VideoParser_Project.settings')

app = Celery('VideoParser_Project')
app.conf.enable_utc = False  # Adjust based on your application's needs
app.conf.update(timezone='UTC')

# Configure Celery using settings, optionally set namespace='CELERY'
app.config_from_object(settings)

# Define your task schedule here:
app.conf.beat_schedule = {
    "process_videos": {
        "task": "Subtitle_ExtractSearch.tasks.process_video",
        'schedule': 1.0,
    },
    "parse_store_subtitle": {
        "task": "Subtitle_ExtractSearch.tasks.parse_time_range",
        "schedule": 1.0,
    },
    "store_the_subtitle": {
        "task": "Subtitle_ExtractSearch.tasks.store_subtitle_in_dynamodb",
        "schedule": 6.0,
    }

}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
