# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 02:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20170218_0103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['nombre'], 'permissions': [('see_profile', 'ver perfil')]},
        ),
    ]