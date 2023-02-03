from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=100)
    leader = models.OneToOneField(
        'users.User', on_delete=models.CASCADE, null=True, blank=True, related_name='team_leader'
    )

    class Meta: 
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name

