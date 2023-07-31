from django.shortcuts import render, redirect
from account.forms import *
from account.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

## home de account, no tiene nada##
def account_home(request):
    return render(request, 'account_home.html')

## perfil ##
@login_required
def profile(request):    
    return render(request, 'profile.html')

## editar foto de perfil##
@login_required
def edit_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatar(user=user, avatar=form.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'edit_profile.html')
    else:
        form = AvatarForm()
    return render(request, 'edit_avatar.html', {'form':form})


##editar perfil##
@login_required
def edit_profile(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']          
            usuario.email = data['email']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2'] 
            usuario.save()
            return render(request, 'profile.html')
    else:
        form = UserEditForm(initial={'first_name': usuario.first_name, 'last_name': usuario.last_name, 'email': usuario.email})

    return render(request, 'edit_profile.html', {'form': form, 'usuario': usuario,'url': avatars[0].avatar.url})











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