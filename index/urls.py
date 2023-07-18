from django.urls import path
from index import views

urlpatterns = [
    path('', views.index_home, name='index_home'),
    path('about', views.about, name='about')
]
