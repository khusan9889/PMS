from django.shortcuts import render
from rest_framework import generics
from .models import Project_docs
from .serializers import Project_docsSerializer

# Create your views here.

#GET,PUT,DELETE methods
class Project_docsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project_docs.objects.all()
    serializer_class = Project_docsSerializer

#POST method
class Project_docsCreateView(generics.CreateAPIView):
    queryset = Project_docs.objects.all()
    serializer_class = Project_docsSerializer