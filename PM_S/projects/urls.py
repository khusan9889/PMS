from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ProjectAPIDetailView.as_view()), #DELETE,GET,PUT methods
    path('post/', ProjectCreateAPIView.as_view()), #Create
]