from django.contrib import admin
from .models import Usuario
# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):

    list_display = ['user', 'nombres', 'apellidos']

    class Meta:
        model = Usuario


admin.site.register(Usuario, UsuarioAdmin)
