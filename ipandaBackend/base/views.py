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
    },
        {
        'Endpoint': 'accounting/',
        'method': 'GET',
        'body': None,
        'description': 'Get All Accounting Urls'
    },
        {
        'Endpoint': 'billing/',
        'method': 'GET',
        'body': None,
        'description': 'Get All Billing Urls'
    },
    {
        'Endpoint': 'inventory/',
        'method': 'GET',
        'body': None,
        'description': 'Get All inventory Urls'
    },
    {
        'Endpoint': 'reports/',
        'method': 'GET',
        'body': None,
        'description': 'Get All Reports Urls'
    }
    ]
    return Response(routes)

