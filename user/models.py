from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=80, blank=True)
    signature = models.TextField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.displayname
