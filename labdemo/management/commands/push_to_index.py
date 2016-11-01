from django.core.management.base import BaseCommand
from labdemo.models import kazpost
from elasticsearch.client import IndicesClient
from django.conf import settings
from labdemo.es_mappings import model_es_indices, es_mappings
from elasticsearch.helpers import bulk
from django.contrib.gis import geos
import json

class Command(BaseCommand):


	def handle(self, *args, **options):
		print("working")


es_ind_settings = {
   "settings": {
       "analysis": {
           "analyzer": {
               "my_analyzer": {
                   "type": "custom",
                   "tokenizer": "standard",
                   "filter": ["lowercase", "my_stopwords", "standard"]
               }
           },
           "filter": {
               "my_stopwords": {
                   "type": "stop",
                   "stopwords": "дом,строение,район,город,улица,область"
               }
           }
       }
   }
}