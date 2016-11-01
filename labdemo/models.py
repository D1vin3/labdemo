from django.contrib.gis import geos
from django.contrib.gis.db import models


class kazpost(models.Model):
    post_index = models.CharField(max_length=10, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    locality = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    house = models.CharField(max_length=20, blank=True, null=True)
    geojson = models.CharField(max_length=500, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        name = self.locality+' '+self.district+' '+self.street+' '+self.street+' '+self.house
        return unicode(name)