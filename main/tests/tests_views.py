from tests.utils import *

from main.views import *


class TestViews(TestCase):
    """Testing main.views"""

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        objectCreator(cls, 'post')
        cls.authenticatedClient = Client()
        cls.authenticatedClient.force_login(cls.user, backend=None)

    def test_index_GET(self):
        """Requesting index page"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_category_GET(self):
        """Requesting category page"""
        response = self.client.get(
            reverse('category', args=[self.category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_create_post_POST(self):
        """Creating post"""
        post_data = {
            'title': data.post_title,
            'category': self.category.id,
            'body': data.post_body
        }

        self.assertRaises(ValueError, lambda: self.client.post(
            reverse('create_post'), data=post_data))

        response = self.authenticatedClient.post(
            reverse('create_post'), data=post_data)
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(str(list(response.wsgi_request._messages)
                         [0]), 'Post created successfully.')

    def test_post_GET(self):
        """Requesting post page"""
        response = self.client.get(
            reverse('post', args=[self.category.name, self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/post.html')

    def test_create_comment_POST(self):
        """Creating comment"""
        comment_data = {
            'body': data.comment_body
        }

        self.assertRaises(ValueError, lambda: self.client.post(
            reverse('create_comment', args=(self.category.name, self.post.id)), data=comment_data))

        response = self.authenticatedClient.post(
            reverse('create_comment', args=(self.category.name, self.post.id)), data=comment_data)
        self.assertRedirects(response, reverse(
            'post', args=(self.category.name, self.post.id)))
        self.assertEqual(str(list(response.wsgi_request._messages)
                         [0]), 'Comment created successfully.')
