from django import forms
from .models import *

class UserForm(forms.ModelForm):    
    gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('I prefer not to tell', 'I prefer not to tell')])
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['name', 'last_name','username', 'email','age', 'avatar', 'password']