from django.contrib import admin
from .models import Proveedor, Cliente, TelefonoCliente, Categoria, Producto, Venta, DetalleVenta

admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(TelefonoCliente)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
