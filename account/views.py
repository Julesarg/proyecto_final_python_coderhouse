from typing import Any, Dict
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import *
from account.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404

## CREAR PROFILE ##
class CreateProfileView(CreateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'create_profile.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

## EDITAR PROFILE ##
class EditProfileView(generic.UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    fields = ['age', 'gender', 'avatar']
    success_url = 'profile'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

## VER PROFILE##
class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        id_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['id_user'] = id_user
        return context
    



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
        return render(request, 'register_success.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})