from django import forms
from  .models import MyModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Username',
            'password': 'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }