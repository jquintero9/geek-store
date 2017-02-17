#!/usr/local/bin/python
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .forms import Regex

# Create your models here.


'''
Modelo Usuario: Este modelo representa
'''


class Usuario(models.Model):

    identificacion = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=40,
                               validators=[RegexValidator(regex=Regex.texto, message=Regex.mensaje_texto)],
                               error_messages={'required': '¿Como te llamas?'})

    apellidos = models.CharField(max_length=40,
                                 validators=[RegexValidator(regex=Regex.texto, messagess=Regex.mensaje_text)],
                                 error_messages={'required': '¿Cúales son tus Apellidos?'})

    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10,
                                validators=[RegexValidator(regex=Regex.telefono, message=Regex.mensaje_telefono)],
                                error_messages={'required': '¿Cual es tu número de celular?'})

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username


