from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Orders


class SuperUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class OrderCreateForm(forms.ModelForm):
    department = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите отдел',
    }))

    class Meta:
        model = Orders
        fields = ('department',)
