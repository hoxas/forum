from django.test import TestCase
from django.test.client import RequestFactory
from main.models import *
from freezegun import freeze_time


class mockData:
    def __init__(self):
        self.username = 'Test User'
        self.password = 'Test Password'
        self.email = 'test@live.com'
        self.displayname = 'Test Displayname'
        self.bio = 'Test Bio'
        self.location = 'Test Location'
        self.signature = 'Test Signature'
        self.category_name = 'Test Category'
        self.category_description = 'Test Category Description'
        self.post_title = 'Test Post Title'
        self.post_body = 'Test Post Body'
        self.comment_body = 'Test Comment Body'


data = mockData()


def objectCreator(self, target: str, data=data):
    _possibilities = ['category', 'profile', 'post', 'comment']

    if target in ['category', 'post', 'comment']:
        self.category = Category.objects.create(name=data.category_name,
                                                description=data.category_description)

    if target in ['profile', 'post', 'comment']:
        self.user = User.objects.create(
            username=data.username,
            password=data.password,
            email=data.email
        )
        self.profile = Profile.objects.create(
            user=self.user,
            displayname=data.displayname,
            bio=data.bio, location=data.location,
            signature=data.signature
        )

    if target in ['post', 'comment']:
        self.post = Post.objects.create(
            title=data.post_title,
            body=data.post_body,
            profile=self.profile,
            category=self.category
        )

    if target == 'comment':
        self.comment = Comment.objects.create(
            profile=self.profile,
            body=data.comment_body,
            post=self.post
        )


def timeCreator(timestring=''):
    timestrings = timestring.split(' ')
    days = hours = minutes = seconds = 0
    for timestring in timestrings:
        if 'd' in timestring:
            days = int(timestring.split('d')[0])
        if 'h' in timestring:
            hours = int(timestring.split('h')[0])
        if 'm' in timestring:
            minutes = int(timestring.split('m')[0])
        if 's' in timestring:
            seconds = int(timestring.split('s')[0])

    return datetime(2020, 1, 1 + days, 0 + hours, 0 + minutes, 0 + seconds, 0, timezone.utc)