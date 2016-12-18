from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'dotodo/index.html')


def register(request):
    return render(request, 'dotodo/register.html')


def login_user(request):
    context = {}
    if request.method == 'POST':
        # sys.stderr.write('Note.')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(request.POST.get('next', 'home'))
    else:
        form = LoginForm()
    context['loginForm'] = form
    return render(request, 'dotodo/login.html', context)
# Inside the settings.py file add:
#LOGIN_REDIRECT_URL = 'home'
#http://stackoverflow.com/questions/15084597/django-error-message-for-login-form


def policy(request):
    return render(request, 'dotodo/privacypolicy.html')


def reset(request):
    return render(request, 'dotodo/reset.html')


# user logged in
@login_required(login_url="login")
def home(request):
    return render(request, 'dotodo/home.html')


@login_required(login_url="login")
def activity(request):
    return render(request, 'dotodo/activity.html')


@login_required(login_url="login")
def task(request):
    return render(request, 'dotodo/task.html')


@login_required(login_url="login")
def settings(request):
    return render(request, 'dotodo/settings.html')


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  # reverse = maps name of the route (dotodo/)
#http://stackoverflow.com/questions/21693342/django-after-login-required-redirect-to-next