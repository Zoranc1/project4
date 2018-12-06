from django.urls import path, include
from .views import checkout_show,submit_payment, my_orders, shipped_product


urlpatterns = [
    path('', checkout_show, name='show_checkout'),
    path('submit_payment/',submit_payment, name='submit_payment'),
    path('my_orders/',my_orders, name='my_orders'),
    path('shipped_product/<int:id>',shipped_product, name='shipped_product'),
    ]