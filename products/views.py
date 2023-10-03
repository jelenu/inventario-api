from rest_framework import generics, permissions
from .models import Categoria
from .serializers import CategoriaSerializer, CategoriaCreateSerializer, CategoriaUpdateSerializer

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
