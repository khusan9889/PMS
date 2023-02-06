from django.urls import path
from .views import *
# from django.conf.urls import url

urlpatterns = [
    path('<int:pk>/', ProjectAPIDetailView.as_view()), #DELETE,GET,PUT methods
    path('post/', ProjectCreateAPIView.as_view()), #Create
    # path(r'swagger/', schema_view),
    
]