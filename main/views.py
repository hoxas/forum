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
    return render(request, 'main/post.html', {'data': data, 'post': data.post})
