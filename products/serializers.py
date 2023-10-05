from rest_framework import serializers
from .models import Categoria, Proveedor, Cliente



##########Categorias##########
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')

class CategoriaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    def create(self, validated_data):

        categoria = Categoria.objects.create(
            nombre=validated_data['nombre'],
        )

        return categoria

class CategoriaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

##########Proveedores##########
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'nombre')

class ProveedorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

    def create(self, validated_data):

        proveedor = Proveedor.objects.create(
            nombre=validated_data['nombre'],
        )

        return proveedor

class ProveedorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


##########Clientes##########

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre')

class ClienteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def create(self, validated_data):

        cliente = Cliente.objects.create(
            nombre=validated_data['nombre'],
        )

        return cliente

class ClienteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'