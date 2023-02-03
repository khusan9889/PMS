from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
# Create your views here.

class UserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
