from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from account.forms import *
from account.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.views import generic
from gallery.models import Item

def admin_tools_home(request):
    return render(request, 'admin_tools_home.html')

class UsersList(LoginRequiredMixin,ListView):
    model = User
    template_name = 'users_home.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class UserDelete(LoginRequiredMixin,DeleteView):
    model = User
    success_url ="/users_home/"     
    template_name = "user_confirm_delete.html"
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class UserUpdate(LoginRequiredMixin,generic.UpdateView):
    model = User
    success_url = reverse_lazy('users_home')
    template_name = 'user_edit.html'
    fields = ['username','first_name','last_name', 'email']
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'



class ItemsList(LoginRequiredMixin,ListView):
    model = Item
    template_name = 'items_home.html'
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class ItemDelete(LoginRequiredMixin,DeleteView):
    model = Item
    success_url ="/items_home/"     
    template_name = "item_confirm_delete.html"
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'

class ItemUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Item
    success_url = reverse_lazy('items_home')
    template_name = 'item_edit.html'
    fields = ['item_name','item_image','item_description', 'item_price','item_stock', 'item_genre','item_material']
    login_url = '../../account/login'
    redirect_field_name = 'redirect_to'