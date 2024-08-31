from django.db import models

class Proveedor(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    pagina_web = models.URLField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion_calle = models.CharField(max_length=100)
    direccion_numero = models.CharField(max_length=10)
    direccion_comuna = models.CharField(max_length=50)
    direccion_ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class TelefonoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.cliente.nombre} - {self.telefono}'

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.OneToOneField(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    numero_factura = models.CharField(max_length=20, primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Factura {self.numero_factura} - {self.cliente.nombre}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.producto.nombre} - {self.venta.numero_factura}'
