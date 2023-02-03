from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    speciality_id = models.CharField(max_length=100)
    team = models.ForeignKey(
        'teams.Teams', on_delete=models.SET_NULL, null=True, related_name='team_members'
    ) 