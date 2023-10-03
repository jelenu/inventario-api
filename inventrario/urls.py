from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserDetailView, UserListView
from products.views import CategoriaDetailView, CategoriaListView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', obtain_auth_token, name='login'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('categories/', CategoriaListView.as_view(), name='category-list'),

    path('categories/<int:pk>/', CategoriaDetailView.as_view(), name='category-detail'),


]
