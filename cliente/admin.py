from django.contrib import admin
from .models import Cliente, Direccion, Departamento, Ciudad

# Register your models here.


class DireccionAdmin(admin.ModelAdmin):

    list_display = ['calle', 'carrera', 'numero', 'barrio']

    class Meta:
        model = Direccion


class CiudadAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'departamento']

    class Meta:
        model = Ciudad


admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Cliente)