from django.contrib.auth.models import User
from django.db import models

from django.templatetags.static import static

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=80, blank=True)
    signature = models.TextField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.displayname

    @property
    def avatar_url(self):
        if self.avatar:
            # REVERT THIS AFTER DEPLOYMENT
            # NEEDED TO DISPLAY TEST DATA PROFILE IMGS
            if str(self.avatar).startswith('http'):
                return self.avatar
            return self.avatar.url
        else:
            return static('images/default_avatar.png')

    @property
    def posts(self):
        from main.models import Post
        return Post.objects.filter(profile=self)

    @property
    def comments(self):
        from main.models import Comment
        return Comment.objects.filter(profile=self)
