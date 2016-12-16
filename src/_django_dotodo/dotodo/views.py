from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'dotodo/index.html')


def register(request):
    return render(request, 'dotodo/register.html')


def login(request):
    return render(request, 'dotodo/login.html')


def policy(request):
    return render(request, 'dotodo/privacypolicy.html')


def reset(request):
    return render(request, 'dotodo/reset.html')


# user logged in
def home(request):
    return render(request, 'dotodo/home.html')


def activity(request):
    return render(request, 'dotodo/activity.html')


def task(request):
    return render(request, 'dotodo/task.html')


def settings(request):
    return render(request, 'dotodo/settings.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) # reverse = maps name of the route (dotodo/)