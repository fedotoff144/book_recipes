from django import forms


class UserRegistration(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='name',
                           widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'имя'}))
    email = forms.EmailField(required=True, label='email', widget=forms.EmailInput(
        attrs={'class': 'field', 'placeholder': 'email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'пароль'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'field', 'placeholder': 'подтвердите пароль'}))
    # gender = forms.CharField(max_length=1)
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # photo = forms.ImageField()
