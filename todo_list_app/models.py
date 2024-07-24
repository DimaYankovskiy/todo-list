from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)


class Task(models.Model):
    content = models.CharField(max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')
