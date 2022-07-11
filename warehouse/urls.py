from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('warehouses/<int:warehouse>', views.warehouse_products, name='warehouse_products'),
    path('products/add_product/', views.add_product, name='add_product'),
    path('products/update_product/<int:pk>', views.update_product, name='update_product'),


]
