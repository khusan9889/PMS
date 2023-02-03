from django.db import models
from specialities.models import Specialities
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    speciality = models.ForeignKey(Specialities, on_delete=models.SET_NULL, null=True, blank=True)
    # speciality_id = models.IntegerField( null=True, blank=True)
    team = models.ForeignKey(
        'teams.Teams', on_delete=models.SET_NULL, null=True, blank=True,related_name='team_members'
    )
    # team = models.IntegerField(
    #     null=True, blank=True
    # )

    class Meta: 
        verbose_name_plural = "Users"

