from django.contrib.gis import geos
from django.contrib.gis.db import models


es_mappings = {
    "kazpost": {
        "properties": {
            "region": {
                "type": "string",
                "analyzer": "my_analyzer"
            },
            'area': {
                "type": "string",
                "analyzer": "my_analyzer"
            },
            'locality': {
                "type": "string",
                "analyzer": "my_analyzer"
            },
            'district': {
                "type": "string",
                "analyzer": "my_analyzer"
            },
            'street': {
                "type": "string",
                "analyzer": "my_analyzer"
            },
            'house': {
                "type": "string",
                "analyzer": "my_analyzer"
            },
        }
    }
}


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
        name = ' '
        if self.locality:
            name += self.locality+' '
        if self.district:
            name += self.district
        if self.street:
            name += self.street
        if self.house:
            name += self.house
        return unicode(name)
    
    def es_repr(self):
        data = {}
        mapping = es_mappings[self.__class__.__name__]
        data['_id'] = self.pk
        for field_name in mapping['properties'].keys():
            data[field_name] = self.field_es_repr(field_name)
        return data
 
    def field_es_repr(self, field_name):
        mapping = es_mappings[self.__class__.__name__]
        config = mapping['properties'][field_name]
 
        field_es_value = getattr(self, field_name)
 
        return field_es_value
 
 
    @classmethod
    def get_es_index(cls):
        return model_es_indices[cls.__name__]['index_name']
 
    @classmethod
    def get_es_type(cls):
        return model_es_indices[cls.__name__]['type']






