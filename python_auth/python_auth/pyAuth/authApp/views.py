# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request, 'auth/home.html', {})


def login_user(request):
    return render(request, 'auth/login.html', {})
