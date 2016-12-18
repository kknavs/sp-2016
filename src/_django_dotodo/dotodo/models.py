from django.db import models
# Create your models here.

from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    finished = models.BooleanField(default=False)
    priority = models.IntegerField()
    video = models.CharField(max_length=100, default='')  # path to video - check FilePathField
    created_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(default=datetime.now)
    updated_date = models.DateTimeField(default=datetime.now)
