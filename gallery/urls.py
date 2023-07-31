from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('search_success/', views.searchByMat, name = 'search_success'),
    path('add_success/', views.add_success, name='add_success'),
    path('search_fail', views.search_fail, name='search_fail'),
    path('add_item', views.add_item, name='add_item'),
    path('paintings/list', views.PaintingList.as_view(), name='paintings'),
    path('sculptures/list', views.SculptureList.as_view(), name='sculptures'),
    path('wood_and_metal/list', views.WoodMetalList.as_view(), name='wood_and_metal'),
    path('digital_assets/list', views.NftList.as_view(), name='digital_assets'),
    path('other_craftings/list', views.OtherList.as_view(), name='other_craftings'),
    path(r'^(?P<pk>\d+)$', views.ItemDetail.as_view(), name='detail_item'),
    path(r'edit/(?P<pk>\d+)$', views.ItemUpdate.as_view(), name='edit'),
    path(r'delete/(?P<pk>\d+)$', views.ItemDelete.as_view(), name='delete')    
]
