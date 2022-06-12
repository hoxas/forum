from tests.utils import *

from user.views import *


class TestViews(TestCase):
    """Testing user.views"""

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        objectCreator(cls, 'profile')
        cls.authenticatedClient = Client().login({'username': cls.user.username,
                                                 'password': data.password}, follow=True)
        print(cls.authenticatedClient)

    def test_auth_GET(self):
        """Requesting auth page"""
        response = self.client.get(reverse('auth'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/auth.html')

        authresponse = self.authenticatedClient.get(reverse('auth'))
        self.assertRedirects(authresponse, '/')
