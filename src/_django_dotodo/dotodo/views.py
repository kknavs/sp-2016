from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm, EditTaskForm, EditCategoryForm

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
    context = {}
    if request.method == 'POST':
        form = EditTaskForm(request.POST, request=request)
        form_cat = EditCategoryForm(request.POST, request=request)
        if form_cat.is_valid():
            cat = form_cat.save()
            if form.is_valid():
                form.save(category=cat)
                return index(request)
    else:
        form_cat = EditCategoryForm()
        form = EditTaskForm()
    context['edit_form'] = form
    context['edit_form_cat'] = form_cat
    return render(request, 'dotodo/task.html', context)


@login_required(login_url="login")
def settings(request):
    return render(request, 'dotodo/settings.html')


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  # reverse = maps name of the route (dotodo/)
    # http://stackoverflow.com/questions/21693342/django-after-login-required-redirect-to-next
