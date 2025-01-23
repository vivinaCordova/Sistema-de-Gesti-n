from django.db import models

# Create your models here.
class Persona (models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)

class Cajero(models.Model):
    codigo_identificacion = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)

    def escanearProducto(self):
        pass

class Cliente(models.Model):
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)

class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50)
    cantidadEnStock = models.IntegerField(default =0)

class Factura(models.Model):
    fecha = models.DateField()
    numero = models.CharField(max_length=50)
    subtotal = models.FloatField()
    impuestos = models.FloatField()
    Total = models.FloatField()

class CajaRegistradora(models.Model):
    numero_de_identificación = models.CharField(max_length=50)
    montoInicial = models.FloatField()
    montoActual = models.FloatField()
    transacciones = models.FloatField()