from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.views import UserDetailView, UserListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL para listar y crear usuarios (solo administradores)
    path('users/', UserListView.as_view(), name='user-list'),

    # URL para ver, actualizar y eliminar usuarios (solo administradores)
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # URL para iniciar sesión (para todos los usuarios)
    path('login/', obtain_auth_token, name='login'),

    
]
