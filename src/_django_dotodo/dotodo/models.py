from django.db import models
# Create your models here.
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone


# https://docs.djangoproject.com/en/1.10/ref/models/fields/#filefield
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    date = models.DateField(default=timezone.datetime.today)
    PRIORITY_CHOICES = (
        ('1', 'Do it now (urgent & important)'),
        ('2', 'Delegate (urgent, but not important)'),
        ('3', 'Decide (important, but not urgent)'),
        ('4', 'Do it later (not important, not urgent)')
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=1)
    finished = models.BooleanField(default=False)
    video = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.SET_NULL, blank=True, null=True)



