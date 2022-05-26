from django.db import models

from user.models import *

from main.utils import *


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    views_unique = models.ManyToManyField(
        Profile, related_name='views_unique', blank=True)

    def __str__(self):
        return self.title

    @property
    def views_unique_count(self):
        return self.views_unique.count()

    @property
    def created_time(self):
        return timeDeltaNow(self.created_on)

    @property
    def created_time_human(self):
        return timeHuman(self.created_time)

    @property
    def comments(self):
        return Comment.objects.filter(post=self)

    @property
    def comments_count(self):
        return self.comments.count()

    @property
    def last_comment(self):
        try:
            return self.comments.order_by('-created_on')[0]
        except IndexError:
            return False

    @property
    def last_comment_user(self):
        if self.last_comment:
            return self.last_comment.profile.displayname
        else:
            return self.profile.displayname

    # caching this property maybe?
    @property
    def last_comment_time(self):
        if self.last_comment:
            creation_time = self.last_comment.created_on
        else:
            creation_time = self.created_on

        return timeDeltaNow(creation_time)

    @property
    def last_comment_time_human(self):
        return timeHuman(self.last_comment_time)


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    @property
    def created_time(self):
        return timeDeltaNow(self.created_on)

    @property
    def created_time_human(self):
        return timeHuman(self.created_time)
