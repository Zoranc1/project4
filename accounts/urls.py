from django.urls import path
from .views import signup_buyer ,signup_seller,profile


urlpatterns = [

    path('signup/buyer/', signup_buyer, name='signup_as_buyer'),
    path('signup/seller', signup_seller, name='signup_as_seller'),
    path('profile/<int:id>', profile, name='profile'),
    
    
    ]
    
    