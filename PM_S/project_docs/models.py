from django.db import models
from projects.models import Projects

class Project_docs(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', blank=True)
    description = models.TextField()
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, blank=True)
    class Meta: 
        verbose_name_plural = "Project Docs"


    def __str__(self):
        return self.name