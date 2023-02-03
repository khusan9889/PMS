from django.db import models

class Specialities(models.Model):
    name = models.CharField(max_length=255)