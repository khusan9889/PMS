from django.db import models
from projects.models import Projects


class Tasks(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=True)
    TO_DO = 0
    IN_PROGRESS = 1
    TEST = 2
    DONE = 3
    STATUS_CHOICES = (
        (TO_DO,'to do'),
        (IN_PROGRESS, 'in progress'),
        (TEST,'test'),
        (DONE,'done'),
    )
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task: Start: {self.start_date} Deadline: {self.deadline}"