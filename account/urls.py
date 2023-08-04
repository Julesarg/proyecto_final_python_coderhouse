from django.urls import path
from account import views
from account.views import ProfileView, EditProfileView, CreateProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name='login'),
    path('<int:pk>/profile', ProfileView.as_view(), name='profile'),
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('<int:pk>/edit_profile', EditProfileView.as_view(), name='edit_profile'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
