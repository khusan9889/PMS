"""PM_S URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Project API Documentation",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=[permissions.AllowAny],
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/project_docs/', include('project_docs.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/specialities/', include('specialities.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/users/', include('users.urls')),

    path('api_schema/', get_schema_view(title='Projects API Documentation', description='Guide for the REST API'), name='projects_api_schema'),
    path('swagger/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'projects_api_schema'}
        ), name='swagger'),

]


