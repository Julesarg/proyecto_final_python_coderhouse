from django.urls import path
from account import views

urlpatterns = [
    path('', views.account_home, name='account_home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
]
