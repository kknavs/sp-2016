from django.db import models
# Create your models here.
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _


# https://docs.djangoproject.com/en/1.10/ref/models/fields/#filefield
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cat_name = models.CharField(max_length=100, default='')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cat_name', 'user',)

    def __str__(self):
        return u'{0}'.format(self.cat_name)


class Task(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    date = models.DateField(default=timezone.datetime.today)
    PRIORITY_CHOICES = (
        ('1', _('Do it now (urgent & important)')),
        ('2', _('Delegate (urgent, but not important)')),
        ('3', _('Decide (important, but not urgent)')),
        ('4', _('Do it later (not important, not urgent)'))
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=1)
    finished = models.BooleanField(default=False)
    video = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)


class Notifications(models.Model):
    PRIORITY_CHOICES = (
        ('1', _('Every day')),
        ('2', _('For important task')),
        ('3', _('No notifications')),
    )
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notifications')


def create_user_notifications(sender, instance, created, **kwargs):
    if created:
        Notifications.objects.create(user=instance)

post_save.connect(create_user_notifications, sender=User)



