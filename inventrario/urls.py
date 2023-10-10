from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserDetailView, UserListView
from products.views import (CategoriaDetailView, CategoriaListView, ProveedorDetailView, ProveedorListView,
                            ClienteDetailView, ClienteListView, ProductoDetailView, ProductoListView,
                            TransaccionEntradaListView, TransaccionEntradaDestroyView, TransaccionSalidaDestroyView, TransaccionSalidaListView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', obtain_auth_token, name='login'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('categories/', CategoriaListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoriaDetailView.as_view(), name='category-detail'),

    path('suppliers/', ProveedorListView.as_view(), name='supplier-list'),
    path('suppliers/<int:pk>/', ProveedorDetailView.as_view(), name='supplier-detail'),

    path('customers/', ClienteListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', ClienteDetailView.as_view(), name='customer-detail'),

    path('products/', ProductoListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductoDetailView.as_view(), name='product-detail'),

    path('input-transactions/', TransaccionEntradaListView.as_view(), name='input-transaction-list'),
    path('input-transactions/<int:pk>/', TransaccionEntradaDestroyView.as_view(), name='input-transaction-detail'),
    
    path('output-transactions/', TransaccionSalidaListView.as_view(), name='output-transaction-list'),
    path('output-transactions/<int:pk>/', TransaccionSalidaDestroyView.as_view(), name='output-transaction-detail'),




]
