from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm,\
    password_reset_complete, password_change_done, password_change

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_user, name='login'),
    # url(r'^register/', views.register, name='register'),
    url(r'^privacy_policy/', views.policy, name='policy'),
    url(r'^password/reset/$', password_reset, {'template_name': 'registration/reset.html'}, name='password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         password_reset_confirm, {'template_name': 'registration/auth_password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^password/reset/complete/$',
        password_reset_complete,{'template_name': 'registration/auth_password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^password/reset/done/$', password_reset_done, {'template_name': 'registration/auth_password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password/change/$', password_change, {'template_name': 'registration/auth_password_change_form.html'},
        name='password_change'),
    url(r'^password/change/done$', password_change_done, {'template_name': 'registration/auth_password_change_done.html'},
        name='password_change_done'),

    # user must be logged in
    url(r'^home/', views.home, name='home'),
    url(r'^task/$', views.task, name='task'),
    url(r'^task/edit/(?P<id>\d+)/$', views.task, name='task_edit'),
    url(r'^category/$', views.category, name='category'),
    # url(r'^category/edit/(?P<id>\d+)/$', views.category, name='category'),
    url(r'^activity/', views.activity, name='activity'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^logout/', views.logout_user, name='logout'),
]
