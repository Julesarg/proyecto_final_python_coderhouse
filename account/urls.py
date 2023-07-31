from django.urls import path
from account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.account_home, name='account_home'),
    path('login', views.login_request, name='login'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('edit_avatar', views.edit_avatar, name='edit_avatar')
]
