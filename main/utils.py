from common.utils import *
from django.core.paginator import Paginator


def paginate(request, objects, per_page=2):
    paginator = Paginator(objects, per_page)
    page = request.GET.get('page')
    objects = paginator.get_page(page)

    return objects


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
                self.comments = paginate(request, comments)
            else:
                posts = Post.objects.filter(
                    category=self.category).order_by('-created_on')
                self.posts = paginate(request, posts)
        else:
            posts = Post.objects.all().order_by('-created_on')
            self.posts = paginate(request, posts)

    # So basically if a post has no category it can't be accessed?
