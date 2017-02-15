#!/usr/local/bin/python
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from usuario.models import Usuario

# Create your models here.


'''
Modelo Administrador: Este modelo representa los usurarios administradores de la empresa.
'''


class Administrador(models.Model):

    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s - %s %s' % (self.usuario.identificacion, self.usuario.nombres, self.usuario.apellidos)


'''
Modelo País: Representa los países de los proveedores a los cuales la empresa compra.
'''


class Pais(models.Model):
    nombre = models.CharField(max_length=30)
    iniciales = models.CharField(max_length=3)

    class Meta:
        db_table = 'paises'
        ordering = ['nombre']

    def __unicode__(self):
        return '%s (%s)' % (self.nombre, self.iniciales)


'''
Modelo Proveedores: Representa los proveedores a quines la empresa compra
los productos.
'''


class Proveedor(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    pais = models.ForeignKey('Pais', on_delete=models.PROTECT)
    telefono = models.CharField(max_length=10)
    pagina_web = models.URLField()

    class Meta:
        ordering = ['nombre']
        db_table = 'proveedores'

    def __unicode__(self):
        return '%s - %s' % (self.nombre, self.pais)


'''
Modelo Categoria: Representa las categorias a las cuales pertenecen
los productos.
'''


class Categoria(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']
        db_table = 'categorias'

    def __unicode__(self):
        return self.nombre


'''
Modelo Producto: Representa los productos que vende la empresa y que los clientes
pueden ver y comprar desde la aplicación.
'''


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.PROTECT)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    descripcion = models.TextField(max_length=240)
    precio = models.PositiveIntegerField()
    estado = models.CharField(max_length=20, default='disponible')
    stock = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['nombre', 'categoria']
        db_table = 'productos'

    def __unicode__(self):
        return '%s - %s - %d' % (self.nombre, self.categoria, self.precio)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["name"]

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

