from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer
# Create your views here.

class TasksAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

class TasksCreateAPIView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

