from dataclasses import field

from rest_framework.serializers import ModelSerializer

from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=self.validated_data['password']
        )
        user.save()
