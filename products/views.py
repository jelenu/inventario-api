from rest_framework import generics, permissions
from .models import Categoria, Proveedor, Cliente, Producto, TransaccionEntrada, TransaccionSalida
from .serializers import (  CategoriaSerializer, CategoriaCreateSerializer, CategoriaUpdateSerializer,
                            ProveedorCreateSerializer, ProveedorSerializer, ProveedorUpdateSerializer,
                            ClienteCreateSerializer, ClienteSerializer, ClienteUpdateSerializer,
                            ProductoCreateSerializer, ProductoSerializer, ProductoUpdateSerializer,
                            TransaccionEntradaCreateSerializer, TransaccionEntradaSerializer, TransaccionEntradaDestroySerialzier,
                            TransaccionSalidaCreateSerializer, TransaccionSalidaDestroySerialzier, TransaccionSalidaSerializer)


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


##########Productos##########
class ProductoListView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductoCreateSerializer
        return ProductoSerializer

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


##########Transaccion Entrada##########
class TransaccionEntradaListView(generics.ListCreateAPIView):
    queryset = TransaccionEntrada.objects.all()
    serializer_class = TransaccionEntradaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TransaccionEntradaCreateSerializer
        return TransaccionEntradaSerializer

class TransaccionEntradaDestroyView(generics.DestroyAPIView):
    queryset = TransaccionEntrada.objects.all()
    serializer_class = TransaccionEntradaDestroySerialzier
    permission_classes = [permissions.IsAdminUser]


##########Transaccion Salida##########
class TransaccionSalidaListView(generics.ListCreateAPIView):
    queryset = TransaccionSalida.objects.all()
    serializer_class = TransaccionSalidaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TransaccionSalidaCreateSerializer
        return TransaccionSalidaSerializer

class TransaccionSalidaDestroyView(generics.DestroyAPIView):
    queryset = TransaccionSalida.objects.all()
    serializer_class = TransaccionSalidaDestroySerialzier
    permission_classes = [permissions.IsAdminUser]