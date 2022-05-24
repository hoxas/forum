from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from main.utils import *

# Create your views here.


def index(request):
    data = Request_Context(request)
    return render(request, 'main/index.html', {'data': data})


def category(request, category_name):
    data = Request_Context(request)
    data.posts = category_name
    return render(request, 'main/category.html', {'data': data})
