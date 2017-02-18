#!usr/bin/local
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from usuario.models import Usuario, Regex
from administrador.models import Producto
from django.core.validators import RegexValidator

'''
Modelo Departamento: Representa los departamentos de Colombia.
'''


class Departamento(models.Model):
    nombre = models.CharField(max_length=30,
                              validators=[RegexValidator(regex=Regex.texto, message=Regex.mensaje_texto)],
                              unique=True)

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre

'''
Modelo Ciudad: Representa las ciudades y los municipios de colombia,
para saber la ubicación de los adminstradores y clientes.
'''


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return '%s (%s)' % (self.nombre, self.departamento)


'''
Modelo Dirección: Representa la dirección de los usuarios administradores y clientes.
'''

'''
class Direccion(models.Model):
    avenida = models.CharField(max_length=30)
    calle = models.CharField(max_length=30, null=True, default='no tiene')
    carrera = models.CharField(max_length=30, null=True, default='no tiene')
    numero = models.CharField(max_length=10)
    barrio = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s # %s %s' % (self.calle, self.numero, self.barrio)
'''

'''
Modelo Cliente: Representa los clientes que acceden a la página para realizar sus compras.
'''


class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    genero = models.CharField(max_length=9)
    fecha_registro = models.DateField(auto_now_add=True)
    direccion = models.TextField(max_length=100)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('see_profile', 'ver perfil')
        ]

    def __unicode__(self):
        return self.usuario.user.username


'''
Modelo Pago: Representa los métodos de pago disponibles para realizar las compras.
'''


class Pago(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=50)

    class Meta:
        ordering = ['nombre']
        db_table = 'pagos'

    def __unicode__(self):
        return self.nombre


'''
Modelo Pedido: Representa los pedidos de los productos que quieren
comprar los clientes.
'''


class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT)
    fecha = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField()
    pago = models.ForeignKey('Pago', on_delete=models.PROTECT)

    class Meta:
        ordering = ['-fecha']
        db_table = 'pedidos'

    def __unicode__(self):
        return 'Pedido: %d - Nombre: %s' % (self.id, self.cliente)


'''
Modelo Producto Pedido: Representa cada uno de los productos que el cliente
ha incluido en el pedido.
'''


class ProductoPedido(models.Model):
    pedido = models.ForeignKey('Pedido')
    producto = models.ForeignKey(Producto)
    cantidad = models.PositiveSmallIntegerField()
    total = models.IntegerField()

    class Meta:
        ordering = ['pedido']
        db_table = 'productos_pedidos'

    def __unicode__(self):
        return '%s - %s' % (self.pedido, self.producto)


