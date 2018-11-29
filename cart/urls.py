from django.urls import path, include
from .views import adding_to_cart,view_cart,remove_from_cart

urlpatterns = [
    path('add/', adding_to_cart, name='adding_to_cart'),
    path('view/', view_cart, name='view_cart'),
    path('remove/<int:id>', remove_from_cart, name='remove_from_cart'),
    ]