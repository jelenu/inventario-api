from rest_framework import serializers
from .models import Categoria, Proveedor, Cliente, Producto, TransaccionEntrada, TransaccionSalida
from django.utils import timezone

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


##########Productos##########
class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nombre')

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'precio', 'sku', 'categoria', 'cantidad_en_stock')


class ProductoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'sku', 'categoria')


class ProductoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'sku', 'categoria')


##########Transaccion Entrada##########
class TransaccionEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionEntrada
        fields = '__all__'


class TransaccionEntradaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionEntrada
        fields = ('producto', 'cantidad', 'proveedor')

    def create(self, validated_data):
        producto = validated_data['producto']
        cantidad = validated_data['cantidad']

        # Asegurarse de que la cantidad de stock sea válida
        if cantidad < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa.")

        # Actualizar la cantidad_en_stock del producto
        producto.cantidad_en_stock += cantidad
        producto.save()

        # Agregar la fecha actual
        validated_data['fecha'] = timezone.now()

        # Crear la transacción de entrada
        transaccion_entrada = TransaccionEntrada.objects.create(**validated_data)

        return transaccion_entrada

class TransaccionEntradaDestroySerialzier(serializers.Serializer):
    mensaje = serializers.CharField(default="Objeto eliminado con éxito")


##########Transaccion Salida##########
class TransaccionSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionSalida
        fields = '__all__'


class TransaccionSalidaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionSalida
        fields = ('producto', 'cantidad', 'cliente')

    def create(self, validated_data):
        producto = validated_data['producto']
        cantidad = validated_data['cantidad']

        # Asegurarse de que la cantidad de stock sea válida
        if cantidad < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa.")

        # Actualizar la cantidad_en_stock del producto
        producto.cantidad_en_stock -= cantidad
        producto.save()

        # Agregar la fecha actual
        validated_data['fecha'] = timezone.now()

        # Crear la transacción de Salida
        transaccion_Salida = TransaccionSalida.objects.create(**validated_data)

        return transaccion_Salida

class TransaccionSalidaDestroySerialzier(serializers.Serializer):
    mensaje = serializers.CharField(default="Objeto eliminado con éxito")