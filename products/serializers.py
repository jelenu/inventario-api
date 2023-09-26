from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class CategoriaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre')

    def create(self, validated_data):

        categoria = Categoria.objects.create(
            nombre=validated_data['nombre'],
        )

        return categoria

class CategoriaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre')
