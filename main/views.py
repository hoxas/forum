from urllib.request import Request
from django.shortcuts import render
from main.utils import *

# Create your views here.


def index(request):
    data = Request_Context(request)
    return render(request, 'main/index.html', {'data': data})


def category(request, category_name):
    data = Request_Context(request, category=category_name)
    return render(request, 'main/index.html', {'data': data})


def post(request, category_name, post_id):
    data = Request_Context(request, category=category_name, post_id=post_id)
    data.post.views += 1
    data.post.save()

    if request.user.is_authenticated:
        if request.user.profile in data.post.views_unique.all():
            pass
        else:
            data.post.views_unique.add(request.user.profile)

    return render(request, 'main/post.html', {'data': data, 'post': data.post})
