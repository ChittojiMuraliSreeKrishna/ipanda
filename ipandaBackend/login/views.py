from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import *
from .models import *
from .models import User
from .serializers import UserSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': 'login/',
            'method': 'POST',
            'body': None,
            'description': 'User Login Page'
        },
        {
            'Endpoint': 'register/',
            'method': 'POST',
            'body': None,
            'description': 'User Registration Page'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def usersList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def registrationPage(request):
    serializer = UserSerializer(data=request.data)
    data = {}
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
