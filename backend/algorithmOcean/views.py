from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccountSerializer, UserSerializer
from .models import Account, CustomUser

# Create your views here.

class Account(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class CustomUser(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    