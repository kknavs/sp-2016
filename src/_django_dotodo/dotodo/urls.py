from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^privacy_policy/', views.policy, name='policy'),
    url(r'^reset/', views.reset, name='reset'),

    url(r'^home/', views.home, name='home'),
    url(r'^task/$', views.task, name='task'),
    url(r'^task/edit/(?P<id>\d+)/$', views.task, name='task'),
    url(r'^category/$', views.category, name='category'),
    # url(r'^category/edit/(?P<id>\d+)/$', views.category, name='category'),
    url(r'^activity/', views.activity, name='activity'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^logout/', views.logout_user, name='logout'),
]
