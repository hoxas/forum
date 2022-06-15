from tests.utils import *

from django.core.exceptions import ObjectDoesNotExist

from user.views import *


class TestViews(TestCase):
    """Testing user.views"""

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        objectCreator(cls, 'profile')
        cls.authenticatedClient = Client()
        cls.authenticatedClient.force_login(cls.user, backend=None)

    def test_auth_GET(self):
        """Requesting auth page"""
        response = self.client.get(reverse('auth'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/auth.html')

        authresponse = self.authenticatedClient.get(reverse('auth'))
        self.assertRedirects(authresponse, '/')

    def test_register_POST(self):
        """Registering new user"""
        # Making sure models cascade is working
        User.objects.get(id=self.user.id).delete()
        self.assertRaises(ObjectDoesNotExist,
                          lambda: User.objects.get(id=self.user.id))
        self.assertRaises(ObjectDoesNotExist,
                          lambda: Profile.objects.get(id=self.profile.id))

        response = self.client.post(reverse('register'))
        self.assertRedirects(response, reverse('auth'))

        response = self.client.post(reverse('register'), data={
            'username': data.username,
            'displayname': data.displayname,
            'email': data.email,
            'password1': data.password,
            'password2': data.password
        })
        # print(response.context)

        self.assertRedirects(response, reverse('index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_POST(self):
        """Logging in user"""
        response = self.client.post(reverse('login'))
        self.assertRedirects(response, reverse('auth'))

        response = self.client.post(reverse('login'), data={
            'username': data.username,
            'password': data.password
        })
        print(response.context)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)
