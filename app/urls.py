from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.main, name='cartridges'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]