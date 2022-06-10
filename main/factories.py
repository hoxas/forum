from django.contrib.auth.models import User
import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from faker import Faker as RealFaker

from main.models import *
from user.models import *

fake = RealFaker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda a: fake.unique.user_name())
    email = factory.Faker('email')
    password = factory.Faker('password')


class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    displayname = factory.Faker('name')
    bio = factory.Faker('text')
    location = factory.Faker('city')
    signature = factory.Faker('text')
    avatar = factory.LazyAttribute(lambda a: static(
        f'images/avatars/{fuzzy.FuzzyInteger(1, 10).fuzz()}.jpg'))


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('text')


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    body = factory.Faker('text')
    profile = fuzzy.FuzzyChoice(Profile.objects.all())
    category = fuzzy.FuzzyChoice(Category.objects.all())
    created_on = factory.Faker(
        'date_time_between', start_date='-5y', end_date='now')
    views = factory.Faker('random_int', min=0, max=100000)

    @factory.post_generation
    def views_unique(self, create, extracted, **kwargs):
        if create:
            return

        if extracted:
            for profile in extracted:
                self.views_unique.add(profile)


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    profile = fuzzy.FuzzyChoice(Profile.objects.all())
    body = factory.Faker('text')
    post = fuzzy.FuzzyChoice(Post.objects.all())

    created_on = factory.Faker(
        'date_time_between', start_date='-5y', end_date='now')
