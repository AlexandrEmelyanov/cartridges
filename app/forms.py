from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


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
