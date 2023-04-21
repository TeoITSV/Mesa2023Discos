from django.db import models

from django.db import models

class SelloDiscografico(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Disco(models.Model):
    nombre_album = models.CharField(max_length=200)
    cantidad_existente = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    anio_edicion = models.IntegerField()
    sello_discografico = models.ForeignKey(SelloDiscografico, on_delete=models.CASCADE)
    genero_musical = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_album


class Interprete(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Venta(models.Model):
    fecha_venta = models.DateField(auto_now_add=True)
    nombre_cliente = models.CharField(max_length=200)
    discos_vendidos = models.ManyToManyField(Disco, through='DetalleVenta')

    def __str__(self):
        return f"Venta a {self.nombre_cliente} el {self.fecha_venta}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} disco(s) {self.disco.nombre_album} vendido(s) a {self.venta.nombre_cliente} el {self.venta.fecha_venta}"
