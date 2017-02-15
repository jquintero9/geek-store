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
        return '%s - %s %s' % (self.usuario.identificacion, self.usuario.nombres, self.usuarios.apellidos)


'''
Modelo País: Representa los países de los proveedores a los cuales la empresa compra.
'''


class Pais(models.Model):
    nombre = models.CharField(max_length=30)
    iniciales = models.CharField(max_length=3)

    def __unicode__(self):
        return '%s (%s)' % (self.nombre, self.iniciales)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

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

