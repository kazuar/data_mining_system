from django.contrib.gis.db import models

class Source(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=30)
    url = models.URLField(null = True)
    objects = models.GeoManager()

class Poi(models.Model):
    name = models.CharField(max_length = 120)
    lon = models.FloatField()
    lat = models.FloatField()
    city = models.CharField(max_length = 120)
    country = models.CharField(max_length = 120)
    objects = models.GeoManager()

    class Meta:
        abstract = True

class SourcePoi(Poi):
    data_source = models.ForeignKey(Source)