from django.core.management.base import BaseCommand
from django.db import transaction

from main.models import *
from user.models import *

from main.factories import *

NUM_USERS = 200
NUM_CATEGORIES = 12
NUM_POSTS = 1000
NUM_COMMENTS = NUM_POSTS * 10


class Command(BaseCommand):
    help = 'Populates forum with test data.'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        models = [User, Profile, Category, Post, Comment]
        for model in models:
            if model == User:
                model.objects.filter(is_superuser=False).delete()
            else:
                model.objects.all().delete()

        self.stdout.write('Creating test data...')

        for _ in range(NUM_USERS):
            ProfileFactory()

        for _ in range(NUM_CATEGORIES):
            CategoryFactory()

        for _ in range(NUM_POSTS):
            PostFactory()

        for _ in range(NUM_COMMENTS):
            CommentFactory()
