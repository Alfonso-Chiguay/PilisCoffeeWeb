from django.contrib import admin
from .models import Colores, Paleta, DetalleDocumento, Documento, LogStockPrecio, Producto, ProductoDescartado, Proveedor, SeqFolio, Trabajador, Venta, VentaProducto

admin.site.register(Colores)
admin.site.register(Paleta)
admin.site.register(DetalleDocumento)
admin.site.register(Documento)
admin.site.register(LogStockPrecio)
admin.site.register(Producto)
admin.site.register(ProductoDescartado)
admin.site.register(Proveedor)
admin.site.register(SeqFolio)
admin.site.register(Trabajador)
admin.site.register(Venta)
admin.site.register(VentaProducto)
