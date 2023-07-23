from django.shortcuts import render
from account.forms import *
from account.models import *
from django.contrib import messages

def account_home(request):
    return render(request, 'account_home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == "POST":
        myForm = UserForm(request.POST, request.FILES)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            user = User(name = inf['name'], last_name = inf['last_name'],username = inf['username'],email = inf['email'], age = inf['age'], password = inf['password'], gender = inf['gender'], avatar = inf['avatar'])
            user.save()
            messages.success(request, f'Welcome to our site {user.name.capitalize()} {user.last_name}, we are happy you joined!')
        return render(request, 'welcome.html', {'myText':f'{myForm.as_p()}'})
    else:
        myForm = UserForm()
    return render(request, 'signup.html', {'myForm': myForm})