from tests.utils import *

from main.utils import *

# Create your tests here.
"""Testing main.utils"""


class TestPaginate(TestCase):
    """Testing main.utils.Paginate"""
    @classmethod
    def setUpTestData(cls):
        objectCreator(cls, 'post')

        for iteration in range(100):
            Post.objects.create(
                title=iteration, body=iteration, profile=cls.profile, category=cls.category)

        cls.request = RequestFactory().get('/')
        cls.objects = Post.objects.all().order_by('-created_on')
        cls.paginate = Paginate(cls.request, cls.objects)
        cls.paginator = cls.paginate.paginator
        cls.pagenumber = cls.paginate.pagenumber

    def test_paginate_properties(self):
        test_paginator = Paginator(self.objects, 20)
        self.assertEqual(self.paginator.num_pages, test_paginator.num_pages)

        # Kinda hacky but does the job for now
        paginator_comparisions = list(zip(self.paginator, test_paginator))
        for comparision in paginator_comparisions:
            self.assertEqual(repr(comparision[0]), repr(comparision[1]))

        self.assertEqual(self.pagenumber, 1)
        self.assertEqual(repr(self.paginate.objects), repr(self.paginator.get_page(
            self.pagenumber)))
        self.assertEqual(self.paginate.elided_page_range, [
                         page for page in self.paginator.get_elided_page_range(self.pagenumber)])


class TestRequestContext(TestCase):
    """Testing main.utils.Request_Context"""

    @classmethod
    def setUpTestData(cls):
        cls.request = RequestFactory().get('/')
        objectCreator(cls, 'comment')
        cls.request.user = cls.user

    def test_request_context_properties(self):
        """Testing main.utils.RequestContext properties"""

        request_index = Request_Context(self.request)
        # Super class properties
        self.assertEqual(request_index.request, self.request)
        self.assertEqual(request_index.user, self.user)

        # Sub class properties
        self.assertQuerysetEqual(request_index.posts,
                                 Post.objects.all().order_by('-created_on'))
        self.assertFalse(request_index.post)
        self.assertFalse(request_index.comments)
        self.assertEqual(request_index.category, 'main')

        self.assertQuerysetEqual(
            request_index.categories, Category.objects.all())
        self.assertEqual(request_index.all_posts_count, Post.objects.count())

    def test_request_context_category(self):
        """Testing main.utils.RequestContext w/ category argument"""

        # Making sure that category object name fetch is case insensitive
        request_category = Request_Context(
            self.request, category=self.category.name.lower())

        self.assertEqual(request_category.category, self.category)
        self.assertQuerysetEqual(request_category.posts, Post.objects.filter(
            category=self.category))
        self.assertFalse(request_category.post)
        self.assertFalse(request_category.comments)

    def test_request_context_post(self):
        """Testing main.utils.RequestContext w/ category & post id"""
        request_post = Request_Context(
            self.request, category=self.category.name.lower(), post_id=self.post.id)
        self.assertEqual(request_post.category, self.category)
        self.assertEqual(request_post.post, self.post)
        self.assertQuerysetEqual(request_post.comments,
                                 Comment.objects.filter(post=self.post))
        self.assertFalse(request_post.posts)
