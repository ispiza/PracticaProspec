from django.contrib import admin
from .models import Venta, DetalleVenta

# Esta clase permite editar los detalles dentro de la misma vista de la Venta
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    # Lista de columnas que se verán en el panel principal
    list_display = ('folio', 'fecha', 'cliente', 'sucursal', 'vendedor', 'metodo_pago', 'total')
    # Incluimos los detalles para que se puedan cargar productos al mismo tiempo
    inlines = [DetalleVentaInline]

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario', 'importe')