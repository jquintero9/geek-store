from django.contrib import admin
from .models import Cliente, Departamento, Ciudad, Pago, Pedido, ProductoPedido

# Register your models here.


'''class DireccionAdmin(admin.ModelAdmin):

    list_display = ['calle', 'carrera', 'numero', 'barrio']

    class Meta:
        model = Direccion
'''


class CiudadAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'departamento']

    class Meta:
        model = Ciudad


class ClienteAdmin(admin.ModelAdmin):

    list_display = ['usuario', 'genero', 'fecha_registro', 'direccion', 'ciudad']

    class Meta:
        model = Cliente


class PedidoAdmin(admin.ModelAdmin):

    list_display = ['cliente', 'fecha', 'fecha_entrega', 'pago']

    class Meta:
        model = Pedido


class ProductoPedidoAdmin(admin.ModelAdmin):

    list_display = ['id', 'pedido', 'producto', 'cantidad', 'total']

    class Meta:
        model = ProductoPedido


'#admin.site.register(Direccion, DireccionAdmin)'
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pago)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ProductoPedido, ProductoPedidoAdmin)
