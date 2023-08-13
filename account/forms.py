from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


# class UserEditForm(UserCreationForm):
#     username = forms.CharField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.PasswordInput()
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']
#         help_texts = {k:"" for k in fields}

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'age', 'gender') 