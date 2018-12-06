from django.urls import path
from .views import make_review

urlpatterns = [
    path('<int:id>', make_review, name='make_review'),
    
    ]