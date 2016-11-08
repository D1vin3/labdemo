from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from rest_framework.renderers import JSONRenderer
from labdemo.models import kazpost
from labdemo.serializers import kazpostSerializer


class SearchView(APIView):
    renderer_classes = (JSONRenderer,)
    def get(self, request):
        term = request.GET.get('text')
        addrs = kazpost.es_search(term)
        kazpost_serializer = kazpostSerializer(addrs, many=True)
        response = {}
        # response['text'] = term
        response['addrs'] = kazpost_serializer.data
        return Response(response)


class IndexView(TemplateView):
    template_name = 'index.html'



