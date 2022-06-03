from urllib.request import Request
from django.contrib import messages
from django.shortcuts import render, redirect
from main.utils import *
from main.forms import *

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


def create_post_POST(request):
    data = Request_Context(request)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = data.profile
            post.save()
            messages.success(
                request, 'Post created successfully.', extra_tags='main')
            return redirect('/')
        elif form.errors:
            for error in form.errors.values():
                messages.error(request,  error,
                               extra_tags='add_post')
            return redirect('/')

        messages.error(request, 'Error creating post.',
                       extra_tags='add_post')
        return redirect('/')
