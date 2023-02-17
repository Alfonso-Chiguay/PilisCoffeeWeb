from django.db import models


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CATEGORIA'


class Colores(models.Model):
    background = models.CharField(max_length=7)
    panel = models.CharField(max_length=7)
    mouse_enter = models.CharField(max_length=7)
    mouse_click = models.CharField(max_length=7)
    id_paleta = models.ForeignKey('Paleta', models.DO_NOTHING, db_column='id_paleta')

    class Meta:
        managed = False
        db_table = 'COLORES'


class DetalleDocumento(models.Model):
    id_documento = models.ForeignKey('Documento', models.DO_NOTHING, db_column='id_documento')
    rut = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='rut')
    codigo_barra = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo_barra')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DETALLE_DOCUMENTO'


class Documento(models.Model):
    id_documento = models.CharField(primary_key=True, max_length=50)
    folio = models.CharField(max_length=255)
    es_factura = models.IntegerField()
    fecha = models.DateField()
    total = models.IntegerField()
    por_pagar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'DOCUMENTO'


class LogStockPrecio(models.Model):
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')
    codigo_barra = models.ForeignKey('Producto', models.DO_NOTHING, db_column='codigo_barra')
    stock_antiguo = models.IntegerField()
    stock_agregado = models.IntegerField()
    precio_antiguo = models.IntegerField()
    precio_nuevo = models.IntegerField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LOG_STOCK_PRECIO'


class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    ruta_img = models.CharField(max_length=255, blank=True, null=True)
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MARCA'


class Paleta(models.Model):
    id_paleta = models.CharField(primary_key=True, max_length=255)
    nombre_paleta = models.CharField(max_length=50)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PALETA'


class Producto(models.Model):
    codigo_barra = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PRODUCTO'


class ProductoDescartado(models.Model):
    codigo_barra = models.ForeignKey(Producto, models.DO_NOTHING, db_column='codigo_barra')
    is_descartado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'PRODUCTO_DESCARTADO'


class Proveedor(models.Model):
    rut = models.CharField(primary_key=True, max_length=8)
    dv = models.CharField(max_length=1)
    razon_social = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'PROVEEDOR'
        unique_together = (('rut', 'dv'),)


class SeqFolio(models.Model):
    nuevo_folio = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'SEQ_FOLIO'


class Trabajador(models.Model):
    id_trabajador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'TRABAJADOR'


class Venta(models.Model):
    folio = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    tipo_venta = models.CharField(max_length=255, db_collation='utf8_spanish_ci')
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'VENTA'


class VentaProducto(models.Model):
    codigo_barra = models.ForeignKey(Producto, models.DO_NOTHING, db_column='codigo_barra')
    folio = models.ForeignKey(Venta, models.DO_NOTHING, db_column='folio')
    cantidad = models.IntegerField()
    valor_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'VENTA_PRODUCTO'

