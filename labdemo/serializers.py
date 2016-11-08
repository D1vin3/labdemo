from rest_framework import serializers
from labdemo.models import kazpost
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework_gis.serializers import GeometrySerializerMethodField
from django.contrib.gis.geos import Point
 
 
class kazpostSerializer(GeoFeatureModelSerializer):
 
    point = GeometrySerializerMethodField()
 
    def get_point(self, obj):
        return Point(obj.lat, obj.lon)
 
    class Meta:
        model = kazpost
        geo_field = "point"
        fields = ('region', 'area', 'locality', 'district', 'street', 'house')