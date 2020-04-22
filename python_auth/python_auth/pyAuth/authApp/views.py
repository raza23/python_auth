# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.


def home(request):
    return render(request, 'auth/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Nice'))
            return redirect('home')
        else:
            messages.success(request, ('Try Again'))

            return redirect('login')
    else:
        return render(request, 'auth/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, ('Logged Out'))
    return redirect('home')
    # Redirect to a success page.


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registered'))
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'form': form}

    return render(request, 'auth/register.html', context)
