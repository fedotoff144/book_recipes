from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True, label='',
                           widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'Имя'}))
    email = forms.EmailField(required=True, label='', widget=forms.EmailInput(
        attrs={'class': 'field', 'placeholder': 'E-mail'}))
    password1 = forms.CharField(required=True, label='', widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, label='', widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'Повторите пароль'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    # gender = forms.CharField(max_length=1)
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # photo = forms.ImageField()


class UserLoginForm(AuthenticationForm):
    # email = forms.EmailField(label='', widget=forms.EmailInput(
    #     attrs={'class': 'field', 'placeholder': 'E-mail'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'field', 'placeholder': 'E-mail'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']