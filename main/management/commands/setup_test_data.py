from django.core.management.base import BaseCommand
from django.db import transaction

from main.models import *
from user.models import *

from main.factories import *

NUM_USERS = 250
NUM_CATEGORIES = 6
NUM_POSTS = 500
NUM_COMMENTS = NUM_POSTS * 200


class Command(BaseCommand):
    help = 'Populates forum with test data.'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        models = [User, Profile, Category, Post, Comment]
        for model in models:
            if model == User:
                superusers = model.objects.filter(is_superuser=True)
                superusers_profiles = [
                    superuser.profile.id for superuser in superusers]
                model.objects.filter(is_superuser=False).delete()
            elif model == Profile:
                model.objects.all().exclude(id__in=superusers_profiles).delete()
            else:
                model.objects.all().delete()

        self.stdout.write('Creating test data...')

        for _ in range(NUM_USERS):
            ProfileFactory()

        self.stdout.write('Created Users and Profiles. 1/4')

        for _ in range(NUM_CATEGORIES):
            CategoryFactory()

        self.stdout.write('Created Categories. 2/4')

        for _ in range(NUM_POSTS):
            PostFactory()

        self.stdout.write('Created Posts. 3/4')

        for _ in range(NUM_COMMENTS):
            CommentFactory()

        self.stdout.write('Created Comments. 4/4')
        self.stdout.write('Done!')
