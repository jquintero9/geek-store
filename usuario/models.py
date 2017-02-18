#!/usr/local/bin/python
# coding: latin-1

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

'''Esta clase contiene las expresiones regulares que ser�n utlizadas
para validar los campos de los formularios.'''


class Regex(object):
    password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&#\-_])[A-Za-z\d$@$!%*?&#\-_]{8,16}'
    mensaje_password = u'La contrase�a debe tener m�ximo un caracter \
    especial($@$!%*?&), una minusc�la, una mayusc�la y un d�gito.'
    texto = r'^[A-Za-z����������\s]+$'
    mensaje_texto = u'Este campo solo admite letras.'
    telefono = r'^[3]([0][0-5]|[1][0-9]|[2][0-2]|[5][01])[\d]{7}$'
    mensaje_telefono = u'El n�mero de celular ingresado no es v�lido.'

'''
Modelo Usuario: Este modelo representa
'''


class Usuario(models.Model):

    identificacion = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=40,
                               validators=[RegexValidator(regex=Regex.texto, message=Regex.mensaje_texto)],
                               error_messages={'required': '�Como te llamas?'})

    apellidos = models.CharField(max_length=40,
                                 validators=[RegexValidator(regex=Regex.texto, message=Regex.mensaje_texto)],
                                 error_messages={'required': '�C�ales son tus Apellidos?'})

    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=10,
                                validators=[RegexValidator(regex=Regex.telefono, message=Regex.mensaje_telefono)],
                                error_messages={'required': '�Cual es tu n�mero de celular?'})

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username


