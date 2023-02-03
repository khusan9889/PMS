from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TasksAPIDetailView.as_view()),
    path('post/', TasksCreateAPIView.as_view()),
]