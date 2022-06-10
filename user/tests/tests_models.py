from tests.utils import *

"""Testing user.models"""


@freeze_time('2020-01-01 12:00:01')
class TestProfile(TestCase):
    """Testing user.models.Profile"""

    @classmethod
    def setUpTestData(cls):
        objectCreator(cls, 'profile')

    def test_profile_str(self):
        """Testing profile string representation"""
        self.assertEqual(str(self.profile), data.displayname)

    def test_profile_properties(self):
        """Testing profile properties"""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.displayname, data.displayname)
        self.assertEqual(self.profile.bio, data.bio)
        self.assertEqual(self.profile.location, data.location)
        self.assertEqual(self.profile.signature, data.signature)
        self.assertEqual(self.profile.date_created, datetime.now(timezone.utc))
        self.assertEqual(self.profile.avatar, '')
        self.assertEqual(self.profile.avatar_url,
                         static('images/default_avatar.png'))

        self.profile.avatar = static('images/my_avatar.png')
        self.assertEqual(self.profile.avatar_url,
                         static('images/my_avatar.png'))
        self.assertQuerysetEqual(self.profile.posts, Post.objects.none())
        self.assertQuerysetEqual(self.profile.comments, Comment.objects.none())
