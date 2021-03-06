# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 12:56
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(error_messages={'required': '\xbfComo te llamas?'}, max_length=40, validators=[django.core.validators.RegexValidator(message='Este campo solo admite letras.', regex='^[A-Za-z\xe1\xe9\xed\xf3\xfa\xc1\xc9\xcd\xd3\xda\\s]+$')])),
                ('apellidos', models.CharField(error_messages={'required': '\xbfC\xfaales son tus Apellidos?'}, max_length=40, validators=[django.core.validators.RegexValidator(message='Este campo solo admite letras.', regex='^[A-Za-z\xe1\xe9\xed\xf3\xfa\xc1\xc9\xcd\xd3\xda\\s]+$')])),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(error_messages={'required': '\xbfCual es tu n\xfamero de celular?'}, max_length=10, validators=[django.core.validators.RegexValidator(message='El n\xfamero de celular ingresado no es v\xe1lido.', regex='^[3]([0][0-5]|[1][0-9]|[2][0-2]|[5][01])[\\d]{7}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
