from django.shortcuts import render, redirect

from user.utils import *

from user.forms import SignUpForm

# Create your views here.


def account(request, profile_displayname=False):
    data = Request_Context(request, profile=profile_displayname)

    if data.profile_search:
        return render(request, 'user/account.html', {'data': data})
    elif data.profile:
        return redirect('/account/' + data.profile + '/')
    else:
        return render(request, 'user/auth.html', {'data': data, 'SignUpForm': SignUpForm})
