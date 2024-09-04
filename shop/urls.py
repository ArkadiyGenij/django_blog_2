from django.urls import path

from shop.apps import ShopConfig
from shop.views import ProductDetailView, ProductListView, ContactView

app_name = ShopConfig.name

urlpatterns = [
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactView.as_view(), name='contact'),
]
