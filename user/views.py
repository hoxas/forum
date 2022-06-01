from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from user.utils import *
from user.models import Profile

from user.forms import SignUpForm, AuthenticationForm, UserChangeForm

# Create your views here.


def auth(request):
    data = Request_Context(request)

    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'user/auth.html', {'data': data, 'AuthenticationForm': AuthenticationForm, 'SignUpForm': SignUpForm})


def register_POST(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user, displayname=form.cleaned_data['displayname'])
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('/')
        messages.error(request, 'Error creating account.')
        return redirect('/account/auth/')

    return redirect('/account/auth/')


def login_POST(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in as {username}')
                return redirect('/')

    messages.error(request, 'Invalid username or password.')

    return redirect('/account/auth/')


def logout_REQUEST(request):
    logout(request)
    return redirect('/')


def account(request, profile_displayname=False):
    data = Request_Context(request, profile=profile_displayname)

    if data.profile_search:
        return render(request, 'user/account.html', {'data': data})
    elif data.profile:
        return redirect('/account/' + data.profile + '/')
    else:
        return redirect('/account/auth/')
