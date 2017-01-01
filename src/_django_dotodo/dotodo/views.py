from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .forms import LoginForm, EditTaskForm, EditCategoryForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task, Category
# Create your views here.


def index(request):
    return render(request, 'dotodo/index.html')


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
def task(request, id=None):
    if id:
        task = get_object_or_404(Task, pk=id)
        if task.user != request.user:
            return HttpResponseForbidden()
    else:
        task = Task(user=request.user)

    form = EditTaskForm(request.POST or None, instance=task, request=request)
    context = {}
    if request.method == 'POST':
        if 'deleteTask' in request.POST:
            task.delete()
            return HttpResponseRedirect(reverse('task'))
        else:
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('task'))
    context['edit_form'] = form
    return render(request, 'dotodo/task.html', context)


@login_required(login_url="login")
def category(request, id=None):
    if id:
        category = get_object_or_404(Category, user=request.user, pk=id)
        if category.user != request.user:
            return HttpResponseForbidden()
    else:
        category = Category(user=request.user)

    form = EditCategoryForm(request.POST or None, instance=category, request=request)
    context = {}
    if request.method == 'POST':
        if request.POST.get('category'):
            category = get_object_or_404(Category, user=request.user, pk=request.POST.get('category'))
            form = EditCategoryForm(request.POST or None, instance=category, request=request)
            if category.user != request.user:
                return HttpResponseForbidden()
        else:
            category = Category(user=request.user)
        if 'deleteCategory' in request.POST:
            category.delete()
            return HttpResponseRedirect(reverse('category'))
        else:
            if form.is_valid():
                test = form.save()
                if test:
                    return HttpResponseRedirect(reverse('category'))
    context['edit_form'] = form
    return render(request, 'dotodo/category.html', context)


@login_required(login_url="login")
def settings(request):
    return render(request, 'dotodo/settings.html')


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  # reverse = maps name of the route (dotodo/)

