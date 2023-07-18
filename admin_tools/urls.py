from django.urls import path
from admin_tools import views

urlpatterns = [
    path('', views.admin_tools_home, name='admin_tools_home'),
    path('edit', views.edit, name='edit')
]
