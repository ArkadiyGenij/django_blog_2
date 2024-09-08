from django.urls import path

from shop.apps import ShopConfig
from shop.views import ProductDetailView, ProductListView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionListView, VersionCreateView, VersionUpdateView, VersionDeleteView

app_name = ShopConfig.name

urlpatterns = [
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('versions/<int:pk>', VersionListView.as_view(), name='version_list'),
    path('versions/create/<int:pk>', VersionCreateView.as_view(), name='version_create'),
    path('versions/edit/<int:pk>', VersionUpdateView.as_view(), name='version_edit'),
    path('versions/delete/<int:pk>', VersionDeleteView.as_view(), name='version_delete')
]
