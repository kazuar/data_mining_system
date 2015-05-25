from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
 
# Indicate Celery to use the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_mining_system.settings')
 
app = Celery('data_mining_system')
app.config_from_object('django.conf:settings')

# This line will tell Celery to autodiscover all your tasks.py that are in your app folders
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)