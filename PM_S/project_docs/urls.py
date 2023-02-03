from django.urls import path 
from .views import *

# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Project Docs')


urlpatterns = [
    path('<int:pk>/', Project_docsAPIDetailView.as_view()), #DELETE,GET,PUT methods
    path('post/', Project_docsCreateView.as_view()),  #Create
    # path('swagger/schema/', schema_view.with_ui('swagger')),
]