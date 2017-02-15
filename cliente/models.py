#!usr/bin/local
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from usuario.models import Usuario



'''
Modelo Dirección: Representa la dirección de los usuarios administradores y clientes.
'''


class Direccion(models.Model):
    calle = models.CharField(max_length=30, null=True, default='no tiene')
    carrera = models.CharField(max_length=30, null=True, default='no tiene')
    numero = models.CharField(max_length=10)
    barrio = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s # %s %s' % (self.calle, self.numero, self.barrio)


'''
Modelo Departamento: Representa los departamentos de Colombia.
'''


class Departamento(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


'''
Modelo Ciudad: Representa las ciudades y los municipios de colombia,
para saber la ubicación de los adminstradores y clientes.
'''


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s (%s)' % (self.nombre, self.departamento)


'''
Modelo Cliente: Representa los clientes que acceden a la página para realizar sus compras.
'''


class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    direccion = models.OneToOneField(Direccion, on_delete=models.PROTECT)
    ciudad = models.ForeignKey('Ciudad', on_delete=models.PROTECT)
