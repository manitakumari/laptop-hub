# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_new_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_product',
            name='image',
            field=models.ImageField(blank=True, upload_to='item_image'),
        ),
    ]
