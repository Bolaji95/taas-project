# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='styles',
            name='styles',
            field=models.ManyToManyField(blank=True, related_name='styles', to='app.Fabrics'),
        ),
    ]
