from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
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


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True, label='', widget=forms.EmailInput(
        attrs={'class': 'field', 'placeholder': 'E-mail'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'Пароль'}))


class UserProfileForm(forms.Form):
    name = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={'class': 'personal-field', 'placeholder': 'Имя'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'personal-field', 'placeholder': 'E-mail', 'required': True}))
    # gender = forms.ChoiceField(label='',choices=[('M', 'Мужчина'), ('F', 'Женщина')], widget=forms.RadioSelect(attrs={'class': 'personal-field'}))
    gender = forms.CharField(label='', max_length=1, widget=forms.TextInput(
        attrs={'class': 'personal-field', 'placeholder': 'Пол'}))
    birthday = forms.DateField(label='', widget=forms.DateInput(
        attrs={'class': 'personal-field', 'placeholder': 'Дата рождения', 'type': 'date'}))
    photo = forms.ImageField(label='', widget=forms.FileInput(
        attrs={'class': 'personal-field', 'placeholder': 'Ваше фото'}))

    # class Meta:
    #     model = User
    #     fields = ['name', 'email', 'gender', 'birthday', 'photo']