# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 04:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0006_auto_20170216_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='Solo se admiten letras.', regex='^[A-Za-z\\s]+$')]),
        ),
    ]