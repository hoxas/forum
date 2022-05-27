from tests.utils import *

# Create your tests here.
"""Testing main.models"""


class TestCategory(TestCase):
    """Testing main.models.Category"""

    @classmethod
    def setUpTestData(cls):
        objectCreator(cls, 'category')

    def test_category_str(self):
        """Testing category string representation"""
        self.assertEqual(str(self.category), data.category_name)

    def test_category_properties(self):
        """Testing category properties"""
        self.assertEqual(self.category.name, data.category_name)
        self.assertEqual(self.category.description, data.category_description)


@freeze_time('2020-01-01 12:00:01')
class TestPost(TestCase):
    """Testing main.models.Post"""

    @classmethod
    def setUpTestData(cls):
        objectCreator(cls, 'post')

    def test_post_str(self):
        """Testing post string representation"""
        self.assertEqual(str(self.post), data.post_title)

    def test_post_properties(self):
        """Testing post properties"""
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
    """Testing main.models.Comment"""

    @classmethod
    def setUpTestData(cls):
        objectCreator(cls, 'comment')

    def test_comment_str(self):
        """Testing comment string representation"""
        self.assertEqual(str(self.comment), str(self.comment.id))

    def test_comment_properties(self):
        """Testing comment properties"""
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
