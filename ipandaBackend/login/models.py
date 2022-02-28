
from django.contrib.auth.models import User
from django.db import models
from httplib2 import RETRIES

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=200, null=True, unique=True)
    password = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(max_length=200, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username[0:50]
