from rest_framework import generics, permissions
from .models import Categoria, Proveedor, Cliente
from .serializers import (  CategoriaSerializer, CategoriaCreateSerializer, CategoriaUpdateSerializer,
                            ProveedorCreateSerializer, ProveedorSerializer, ProveedorUpdateSerializer,
                            ClienteCreateSerializer, ClienteSerializer, ClienteUpdateSerializer)


##########Categorias##########
class CategoriaListView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategoriaCreateSerializer
        return CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


##########Proveedores##########
class ProveedorListView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProveedorCreateSerializer
        return ProveedorSerializer

class ProveedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


##########Clientes##########

class ClienteListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClienteCreateSerializer
        return ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteUpdateSerializer
    permission_classes = [permissions.IsAdminUser]