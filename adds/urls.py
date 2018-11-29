from django.urls import path
from .views import read_ad, edit_ad, write_ad, get_unpublished_ad, publish_ad,show_all_ads

urlpatterns = [
    path('unpublished', get_unpublished_ad, name='get_unpublished_ad'),
    path('write/', write_ad, name='write_ad'),
    path('all', show_all_ads, name='all_ads'),
    path('<int:id>', read_ad, name='read_ad'),
    path('<int:id>/edit/', edit_ad, name='edit_ad'),
    path('<int:id>/publish/', publish_ad, name='publish_ad'),
    
    ]