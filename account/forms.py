from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email','password1', 'password2']
        help_texts = {k:"" for k in fields}

