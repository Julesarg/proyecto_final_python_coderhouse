from django.shortcuts import render
from account.forms import *
from account.models import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def account_home(request):
    return render(request, 'account_home.html')
def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == "POST":
        myForm = UserForm(request.POST, request.FILES)
        if myForm.is_valid():
            inf = myForm.cleaned_data
            user = User(name = inf['name'], last_name = inf['last_name'],username = inf['username'],email = inf['email'], age = inf['age'], password = inf['password'], gender = inf['gender'], avatar = inf['avatar'])
            user.save()
            messages.success(request, 'login.html', f'Welcome to our site {user.name.capitalize()} {user.last_name}, we are happy you joined!')
        return render(request, 'login.html', {'myText':f'{myForm.as_p()}'})
    else:
        myForm = UserForm()
    return render(request, 'signup.html', {'myForm': myForm})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=passw)

            if user is not None:
                login(request, user)
                return render(request, 'login_success.html',  {'form': form})
            else:
                return render(request, 'login_success.html',  {'form': form} )
        else:
            return render(request, 'login_success.html',  {'form': form})
    form = AuthenticationForm()
    return render (request, 'login.html', {'form': form})