from django.urls import path
from pages import views

urlpatterns = [
    path('', views.pages_home, name='pages_home'),
    path('1', views.page1, name='1'),
    path('2', views.page2,name='2'),
    path('3', views.page3,name='3'),
    path('add_p', views.add_p, name='add_p')
]
