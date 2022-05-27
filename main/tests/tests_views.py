from tests.utils import *

from main.views import *


class TestViews(TestCase):
    """Testing main.views"""

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        objectCreator(cls, 'post')
        # cls.client.login(username=data.username, password=data.password)

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

    def test_post_GET(self):
        """Requesting post page"""
        response = self.client.get(
            reverse('post', args=[self.category.name, self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/post.html')
