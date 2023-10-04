from django.shortcuts import render
from rest_framework import generics
from .models import ModifiedUser
from .serializers import ModifiedUserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = ModifiedUser.objects.all()
    serializer_class = ModifiedUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModifiedUser.objects.all()
    serializer_class = ModifiedUserSerializer


