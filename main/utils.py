from .models import *


class Request_Context:
    def __init__(self, request):
        self.request = request
        self.user = request.user

    @property
    def categories(self):
        return Category.objects.all()

    @property
    def posts(self):
        return self.posts

    @posts.setter
    def posts(self, category_name):
        return Post.objects.filter(category__name=category_name)
