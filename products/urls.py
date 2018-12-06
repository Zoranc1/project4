from django.urls import path
from .views import show_all_products, products_by_category, view_product, edit_product, write_product, get_unpublished_products, publish_product

urlpatterns = [
    path('all', show_all_products, name='all_products'),
    path('category/<category>', products_by_category, name='products_by_category'),
    path('<int:id>', view_product, name='view_product'),
    path('<int:id>/edit', edit_product, name='edit_ad'),
    path('write', write_product, name='write_product'),
    path('unpublished', get_unpublished_products, name='get_unpublished_products'),
    path('<int:id>/publish', publish_product, name='publish_product'),
    ]