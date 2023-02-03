from django.shortcuts import render
from rest_framework import generics
from .models import Specialities
from .serializers import SpecialitiesSerializer
# Create your views here.

class SpecialitiesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitiesSerializer

class SpecialitiesCreateAPIView(generics.CreateAPIView):
    queryset = Specialities.objects.all()
    serializer_class = SpecialitiesSerializer
