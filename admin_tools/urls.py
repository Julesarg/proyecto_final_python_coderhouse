from django.urls import path
from admin_tools import views
from gallery.views import *

urlpatterns = [
    path('', views.admin_tools_home, name='admin_tools_home'),
    path('users_home', views.UsersList.as_view(), name='users_home'),
    path(r'user_confirm_delete/(?P<pk>\d+)$', views.UserDelete.as_view(), name='user_confirm_delete'),
    path(r'user_edit/(?P<pk>\d+)$', views.UserUpdate.as_view(), name='user_edit'),
    path('items_home', views.ItemsList.as_view(), name='items_home'),
    path(r'item_confirm_delete/(?P<pk>\d+)$', views.ItemDelete.as_view(), name='item_confirm_delete'),
    path(r'item_edit/(?P<pk>\d+)$', views.ItemUpdate.as_view(), name='item_edit'),

]
