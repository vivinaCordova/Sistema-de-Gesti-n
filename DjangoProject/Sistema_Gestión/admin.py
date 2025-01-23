from django.contrib import admin

# Register your models here.
from .models import (
Persona, Cajero, Cliente, CajaRegistradora, Factura,Producto
)

# Configuración del modelo Persona
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'apellido')
    search_fields = ('nombre', 'cedula', 'apellido')
    list_filter = ('nombre','cedula', 'apellido')

# Configuración del modelo Cajero
@admin.register(Cajero)
class CajeroAdmin(admin.ModelAdmin):
    list_display = ('codigo_identificacion','turno',)
    search_fields = ('codigo_identificacion','turno',)
    list_filter = ('codigo_identificacion','turno',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    List_display = ('email', 'telefono',)
    search_fields = ('email', 'telefono',)

# Configuración del modelo Caja
@admin.register(CajaRegistradora)
class CajaRegistradoraAdmin(admin.ModelAdmin):
    list_display = ('numero_de_identificación','montoInicial', 'montoActual','transacciones',)
    search_fields = ('numero_de_identificación','montoInicial', 'montoActual','transacciones')
    list_filter = ('numero_de_identificación','montoInicial', 'montoActual','transacciones')


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'numero', 'subtotal', 'impuestos', 'Total')
    search_fields = ('fecha', 'numero')
    list_filter = ('fecha',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'categoria', 'cantidadEnStock')
    search_fields = ('codigo', 'nombre', 'categoria')


