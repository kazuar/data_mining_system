from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=30)
    url = models.URLField(null = True)
