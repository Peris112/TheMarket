from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('home/', views.home, name='home'),
    path('terms/', views.terms, name='terms'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),

]