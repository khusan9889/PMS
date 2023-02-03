from django.db import models
from teams.models import Teams
# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)
    team_id = models.ForeignKey(Teams, on_delete=models.CASCADE)