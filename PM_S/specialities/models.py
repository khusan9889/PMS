from django.db import models

class Specialities(models.Model):
    name = models.CharField(max_length=255,default='')

    class Meta: 
        verbose_name_plural = "Specialities"
    
    def __str__(self):
        return self.name

