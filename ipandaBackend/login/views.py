
from multiprocessing import context

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from login import serializers

from .forms import *
from .models import *
from .models import User
from .serializers import UserSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/login',
            'method': 'POST',
            'body': None,
            'description': 'User Login Page'
        },
        {
            'Endpoint': '/signup',
            'method': 'POST',
            'body': None,
            'description': 'User Registration Page'
        }
    ]
    return Response(routes)


@api_view(['POST'])
def registrationPage(request):
    data = request.data
    serializer = UserSerializer(data, many=False)
    if serializer.is_valid():
        serializer.save()
        data['response'] = "Successfully Created the User"
    else:
        data = serializer.errors
    return Response(data)

@api_view(['POST'])
def loginPage(request):
    data = request.data
    return Response(data)