from tests.utils import *

from user.utils import *

"""Testing user.utils"""


class TestRequestContext(TestCase):
    """Testing user.utils.Request_Context"""

    @classmethod
    def setUpTestData(cls):
        cls.request = RequestFactory().get('/')
        objectCreator(cls, 'comment')
        cls.unauth_user = FakeUnauthUser()

    def test_request_context_properties(self):
        """Testing user.utils.RequestContext properties"""

        self.request.user = self.unauth_user

        data_unauthenticated = Request_Context(self.request)
        # Super class properties
        self.assertEqual(data_unauthenticated.request, self.request)
        self.assertEqual(data_unauthenticated.user, self.unauth_user)

        # Sub class properties
        data_unauthenticated_profile_search = Request_Context(
            self.request, profile=self.profile.displayname)
        self.assertFalse(data_unauthenticated_profile_search.profile_search)

        self.request.user = self.user

        data_authenticated = Request_Context(self.request)
        self.assertFalse(data_authenticated.profile_search)

        data_authenticated_profile_search = Request_Context(
            self.request, profile=self.profile.displayname)

        self.assertEqual(
            data_authenticated_profile_search.profile_search, self.profile)
