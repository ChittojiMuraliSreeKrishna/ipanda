from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'barcodes/',
            'method': 'GET',
            'body': None,
            'description': 'Gets All the available barcodes'
        },
        {
            'Endpoint': 'addbarcode/',
            'method': 'POST',
            'body': None,
            'description': 'Adds new Barcode'
        },
        {
            'Endpoint': 'rebarcodes/',
            'method': 'GET',
            'body': None,
            'description': 'Gets All the edited Barcodes'
        },
        {
            'Enddpoint': 'barcode/delete/<str: pk>',
            'method': 'POST',
            'body': None,
            'description': 'Deleted the barcode'
        },
        {
            'Endpoint': 'barcode/edit/<str: pk>',
            'method': 'PUT',
            'body': None,
            'description': 'Edits the barcode'
        },
        {
            'Endpoint': 'barcode/view/<str: pk>',
            'method': 'GET',
            'body': None,
            'description': 'Get the Single barcode data'
        }
    ]
    return Response(routes)
