from django.shortcuts import render, redirect
from account.forms import *
from account.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.save()
            return render(request, 'profile.html')
    else:
        form = UserEditForm(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})

    return render(request, 'edit_profile.html', {'form': form, 'usuario': usuario})

def account_home(request):
    return render(request, 'account_home.html')

def profile(request):
    return render(request, 'profile.html')




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
                return render(request, 'login_error.html',  {'form': form} )
        else:
            return render(request, 'login_error.html',  {'form': form})
    form = AuthenticationForm()
    return render (request, 'login.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            # user = form.save()
            # login(request, user)
            # return redirect('/index_home')
        return render(request, 'register_success.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})