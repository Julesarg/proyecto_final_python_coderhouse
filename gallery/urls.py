from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('paintings', views.paintings, name='paintings'),
    path('sculptures', views.sculptures,name='sculptures'),
    path('woodcraft', views.woodcraft,name='woodcraft'),
    path('digital_assets', views.digital_assets,name='digital_assets'),
    path('other_craftings', views.other_craftings,name='other_craftings'),
    path('add_p', views.add_p, name='add_p')
]
