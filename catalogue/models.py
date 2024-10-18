from django.utils import timezone

from django.db import models

# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now())
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
