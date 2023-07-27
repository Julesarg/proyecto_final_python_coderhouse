from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    path('search/', views.searchByMat, name = 'search'),
    path('search_fail', views.search_fail, name='search_fail'),
    path('add_p', views.add_p, name='add_p'),
    path('paintings/list', views.PaintingList.as_view(), name='paintings'),
    path('sculptures/list', views.SculptureList.as_view(), name='sculptures'),
    path('wood_and_metal/list', views.WoodMetalList.as_view(), name='wood_and_metal'),
    path('digital_assets/list', views.NftList.as_view(), name='digital_assets'),
    path('other_craftings/list', views.OtherList.as_view(), name='other_craftings'),
    path(r'^(?P<pk>\d+)$', views.ItemDetail.as_view(), name='detail_item'),



    # path(r'^new$', views.CourseCreate.as_view(), name='new'),
    # path(r'edit/(?P<pk>\d+)$', views.CourseUpdate.as_view(), name='edit'),
    # path(r'delete/(?P<pk>\d+)$', views.CourseDelete.as_view(), name='delete')
]
