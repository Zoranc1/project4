from django.urls import path, include
from .views import signup_buyer, show_profile,signup_seller,signup_buyer


urlpatterns = [

    path('signup/buyer/', signup_buyer, name='signup_as_buyer'),
    path('signup/seller', signup_seller, name='signup_as_seller'),
    path('profile/', show_profile, name='profile'),
    
    
    ]
    
    