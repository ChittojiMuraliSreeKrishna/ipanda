from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': 'stores/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of stores'
        },
        {
            'Endpoint': 'store/create/',
            'method': 'POST',
            'body': {'state': "", 'district': '', 'city': '', 'area': '', 'phone': '', 'address': '', 'domain': '', 'storename': '', 'gstnumber': ''},
            'description': 'Create new store with data sent in post request'
        },
        {
            'Endpoint': 'store/id/',
            'method': 'GET',
            'body': None,
            'description': 'Return a single store object'
        },
        {
            'Endpoint': 'store/id/update/',
            'method': 'PUT',
            'body': {'state': "", 'district': '', 'city': '', 'area': '', 'phone': '', 'address': '', 'domain': '', 'storename': '', 'gstnumber': ''},
            'description': 'Update an existing store with data sent in post'
        },
        {
            'Endpoint': 'store/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an exiting store'
        },
        {
            'Endpoint': 'stores/filter/',
            'method': 'GET',
            'body': None,
            'description': 'filter the stores with the details'
        },
        {
            'Endpoint': 'domain/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of domains'
        },
        {
            'Endpoint': 'domain/create/',
            'method': 'POST',
            'body': {'domain': "", 'description': ''},
            'description': 'Create new domain with data sent in post request'
        },
    ]

    return Response(routes)
