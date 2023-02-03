from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=100)
    leader = models.OneToOneField(
        'users.User', on_delete=models.CASCADE, null=True, related_name='team_leader'
    )

