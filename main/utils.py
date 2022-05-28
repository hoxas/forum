from common.utils import *


class Request_Context(Request_Context_Generic):
    def __init__(self, request, **kwargs):
        super().__init__(request)
        from main.models import Category, Post, Comment
        self.category = self.post = self.comments = self.posts = False

        if kwargs.get('category', False):
            self.category = Category.objects.get(
                name__iexact=kwargs['category'])
            if kwargs.get('post_id', False):
                self.post = Post.objects.get(id=kwargs['post_id'])
                self.comments = Comment.objects.filter(post=self.post)
            else:
                self.posts = Post.objects.filter(
                    category=self.category)
        else:
            self.posts = Post.objects.all().order_by('-created_on')

    # So basically if a post has no category it can't be accessed?

    @property
    def categories(self):
        from main.models import Category
        return Category.objects.all()
