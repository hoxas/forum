from tests.utils import *

from main.utils import *

# Create your tests here.


class TestRequestContext(TestCase):
    def setUp(self):
        self.request = RequestFactory().get('/')
        objectCreator(self, 'comment')
        self.request.user = self.user

    def test_request_context_properties(self):
        request_index = Request_Context(self.request)
        # Super class properties
        self.assertEqual(request_index.request, self.request)
        self.assertEqual(request_index.user, self.user)

        # Sub class properties
        self.assertQuerysetEqual(request_index.posts,
                                 Post.objects.all().order_by('-created_on'))
        self.assertFalse(request_index.category)
        self.assertFalse(request_index.post)
        self.assertFalse(request_index.comments)

        self.assertQuerysetEqual(
            request_index.categories, Category.objects.all())

        request_category = Request_Context(
            self.request, category=self.category.name)
        self.assertEqual(request_category.category, self.category)
        self.assertQuerysetEqual(request_category.posts, Post.objects.filter(
            category=self.category))
        self.assertFalse(request_category.post)
        self.assertFalse(request_category.comments)

        request_post = Request_Context(
            self.request, category=self.category.name, post_id=self.post.id)
        self.assertEqual(request_post.category, self.category)
        self.assertEqual(request_post.post, self.post)
        self.assertQuerysetEqual(request_post.comments,
                                 Comment.objects.filter(post=self.post))
        self.assertFalse(request_post.posts)
