# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hobby',
            options={'verbose_name': 'Hobby', 'verbose_name_plural': 'Hobbies'},
        ),
    ]
