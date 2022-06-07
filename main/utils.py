from common.utils import *
from django.core.paginator import Paginator


class Paginate:
    def __init__(self, request, objects, per_page=20):
        self.paginator = Paginator(objects, per_page)
        self.pagenumber = request.GET.get('page')
        if self.pagenumber is None:
            self.pagenumber = 1
        self.objects = self.paginator.get_page(self.pagenumber)
        get_elided_page_range = self.paginator.get_elided_page_range(
            self.pagenumber)
        self.elided_page_range = [page for page in get_elided_page_range]


class Request_Context(Request_Context_Generic):
    def __init__(self, request, **kwargs):
        super().__init__(request)
        from main.models import Category, Post, Comment
        self.post = self.comments = self.posts = False
        self.category = 'main'

        if kwargs.get('category', False):
            self.category = Category.objects.get(
                name__iexact=kwargs['category'])
            if kwargs.get('post_id', False):
                self.post = Post.objects.get(id=kwargs['post_id'])
                comments = Comment.objects.filter(
                    post=self.post).order_by('created_on')
                pagination = Paginate(request, comments)
                self.page_range = pagination.elided_page_range
                self.comments = pagination.objects
            else:
                posts = Post.objects.filter(
                    category=self.category).order_by('-created_on')
                pagination = Paginate(request, posts)
                self.page_range = pagination.elided_page_range
                self.posts = pagination.objects
        else:
            posts = Post.objects.all().order_by('-created_on')
            pagination = Paginate(request, posts)
            self.page_range = list(pagination.elided_page_range)
            self.posts = pagination.objects

    # So basically if a post has no category it can't be accessed?
