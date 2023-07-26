from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.gallery_home, name='gallery_home'),
    # path('paintings', views.paintings, name='paintings'),
    # path('sculptures', views.sculptures,name='sculptures'),
    # path('wood_and_metal', views.wood_and_metal,name='wood_and_metal'),
    # path('digital_assets', views.digital_assets,name='digital_assets'),
    # path('other_craftings', views.other_craftings,name='other_craftings'),
    path('add_p', views.add_p, name='add_p'),



    path('paintings/list', views.PaintingList.as_view(), name='paintings'),
    path('sculptures/list', views.SculptureList.as_view(), name='sculptures'),
    path('wood_and_metal/list', views.WoodMetalList.as_view(), name='wood_and_metal'),
    path('digital_assets/list', views.NftList.as_view(), name='digital_assets'),
    path('other_craftings/list', views.OtherList.as_view(), name='other_craftings'),



    path(r'^(?P<pk>\d+)$', views.CourseDetail.as_view(), name='detail'),
    path(r'^new$', views.CourseCreate.as_view(), name='new'),
    path(r'edit/(?P<pk>\d+)$', views.CourseUpdate.as_view(), name='edit'),
    path(r'delete/(?P<pk>\d+)$', views.CourseDelete.as_view(), name='delete')
]
