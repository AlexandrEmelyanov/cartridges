from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.main, name='cartridges'),
    path('create/', views.create_order, name='create-order'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
