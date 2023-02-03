from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', SpecialitiesAPIDetailView.as_view()),
    path('post', SpecialitiesCreateAPIView.as_view()),
]