from rest_framework import generics
from .models import Projects
from .serializers import ProjectsSerializer
#Swagger views

# from rest_framework_swagger.views import get_swagger_view

# Create your views here.

class ProjectAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


# schema_view = get_swagger_view(title='Projects API')


