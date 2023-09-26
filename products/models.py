from django.db import models
 
# Tabla de Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    

# Tabla de Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=255, unique=True)
    cantidad_en_stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Tabla de Proveedores
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# Tabla de Clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 

# Tabla de Transacciones de Entrada
class TransaccionEntrada(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

# Tabla de Transacciones de Salida
class TransaccionSalida(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
