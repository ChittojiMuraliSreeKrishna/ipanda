from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [{
        'Endpoint': 'user/',
        'method': None,
        'body': None,
        'descriptionn': 'Get User Register && Login Urls'
    }]
    return Response(routes)
