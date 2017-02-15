#!/usr/local/bin/python
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


'''
Modelo Usuario: Este modelo representa
'''


class Usuario(models.Model):

    identificacion = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username


