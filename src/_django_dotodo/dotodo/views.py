from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task, Category, Notifications
import logging
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
    return render(request, 'registration/reset.html')


# user logged in
@login_required(login_url="login")
def home(request):
    task_list = Task.objects.filter(user=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(task_list, 10)
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    return render(request, 'dotodo/home.html', {'tasks': tasks})
    #return render(request, 'dotodo/home.html')


@login_required(login_url="login")
def activity(request):
    # logger = logging.getLogger('DOTODO_log')
    # logger.error("Visited activity - "+request.user.username)
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
    notifications = get_object_or_404(Notifications, user=request.user)
    if notifications.user != request.user:
            return HttpResponseForbidden()
    #else:
    # task = Task(user=request.user)
    formU = EditUsernameForm(request.POST or None, instance=request.user)
    form = EditNotificationsForm(request.POST or None, instance=notifications, request=request)
    context = {}
    if request.method == 'POST':
        if 'submitUsername' in request.POST:
            formU.save()
            return HttpResponseRedirect(reverse('settings'))
        else:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('settings'))
    context['edit_form'] = form
    context['edit_u'] = formU
    return render(request, 'dotodo/settings.html', context)


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))  # reverse = maps name of the route (dotodo/)

