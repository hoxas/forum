from common.utils import Request_Context_Generic


class Request_Context(Request_Context_Generic):
    def __init__(self, request, **kwargs):
        super().__init__(request)
        from .models import Post, Comment
        if kwargs.get('category', False):
            if kwargs.get('post_id', False):
                self.post = Post.objects.get(id=kwargs['post_id'])
                self.comments = Comment.objects.filter(post=self.post)
            else:
                self.posts = Post.objects.filter(
                    category__name=kwargs['category'])
        else:
            self.posts = Post.objects.all().order_by('-created_on')
