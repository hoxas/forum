from django.test import TestCase

from freezegun import freeze_time
from datetime import timezone

from main.models import *

# Create your tests here.


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


def objectCreator(self):
    if self.__class__ in [TestCategory, TestPost, TestComment]:
        self.category = Category.objects.create(name=data.category_name,
                                                description=data.category_description)
    if self.__class__ in [TestPost, TestComment]:
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

        self.post = Post.objects.create(
            title=data.post_title,
            body=data.post_body,
            profile=self.profile,
            category=self.category
        )

    if self.__class__ in [TestComment]:
        self.comment = Comment.objects.create(
            profile=self.profile,
            body=data.comment_body,
            post=self.post
        )


class TestCategory(TestCase):
    def setUp(self):
        objectCreator(self)

    def test_category_str(self):
        self.assertEqual(str(self.category), data.category_name)

    def test_category_properties(self):
        self.assertEqual(self.category.name, data.category_name)
        self.assertEqual(self.category.description, data.category_description)


@freeze_time('2020-01-01 12:00:01')
class TestPost(TestCase):
    def setUp(self):
        objectCreator(self)

    def test_post_str(self):
        self.assertEqual(str(self.post), data.post_title)

    def test_post_properties(self):
        self.assertEqual(self.post.title, data.post_title)
        self.assertEqual(self.post.body, data.post_body)
        self.assertEqual(self.post.profile, self.profile)
        self.assertEqual(self.post.category, self.category)
        self.assertEqual(self.post.created_on, datetime.now(timezone.utc))
        self.assertEqual(self.post.last_modified, datetime.now(timezone.utc))
        self.assertEqual(self.post.views, 0)
        self.assertEqual(self.post.views_unique.exists(), False)

        self.assertEqual(self.post.views_unique_count, 0)
        self.assertEqual(self.post.created_time,
                         timeDeltaNow(self.post.created_on))
        self.assertEqual(self.post.created_time_human,
                         timeHuman(self.post.created_time))
        self.assertEqual(self.post.comments.exists(), False)
        self.assertEqual(self.post.comments_count, 0)
        self.assertEqual(self.post.last_comment, False)
        self.assertEqual(self.post.last_comment_user, data.displayname)
        self.assertEqual(self.post.last_comment_time,
                         timeDeltaNow(self.post.created_on))
        self.assertEqual(self.post.last_comment_time_human,
                         timeHuman(self.post.last_comment_time))


@freeze_time('2020-01-01 12:00:01')
class TestComment(TestCase):
    def setUp(self):
        objectCreator(self)

    def test_comment_str(self):
        self.assertEqual(str(self.comment), str(self.comment.id))

    def test_comment_properties(self):
        self.assertEqual(self.comment.profile, self.profile)
        self.assertEqual(self.comment.body, data.comment_body)
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.created_on, datetime.now(timezone.utc))
        self.assertEqual(self.comment.last_modified,
                         datetime.now(timezone.utc))
        self.assertEqual(self.comment.created_time,
                         timeDeltaNow(self.comment.created_on))
        self.assertEqual(self.comment.created_time_human,
                         timeHuman(self.comment.created_time))
