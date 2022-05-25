from django.shortcuts import render

from main.utils import *

# Create your views here.


def user(request, user_id):
    data = Request_Context(request)

    return render(request, 'user/user.html', {'title': 'User'})
