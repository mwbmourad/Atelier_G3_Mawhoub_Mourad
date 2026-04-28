from django.urls import path
from .views import ProductsListView, ProductDetailsView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('product/<int:pk>', ProductDetailsView.as_view(), name='product_detail'),
]