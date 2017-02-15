from django.contrib import admin
from .models import Administrador, Author, Book, Publisher, Proveedor, Pais, Categoria, Producto

# Register your models here.


class ProveedorAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'pais', 'telefono', 'pagina_web']

    class Meta:
        model = Proveedor


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'descripcion']

    class Meta:
        model = Categoria


class ProductoAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'proveedor', 'categoria', 'descripcion', 'precio', 'stock', 'estado']

    class Meta:
        model = Producto


admin.site.register(Administrador)
admin.site.register(Pais)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
