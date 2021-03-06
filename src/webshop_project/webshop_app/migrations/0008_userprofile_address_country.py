# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-05 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshop_app', '0007_remove_userprofile_addrss_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address_country',
            field=models.DecimalField(choices=[(0.12, 'United States'), (0.14, 'Europe'), (0.3, 'Asia')], decimal_places=2, default=0.12, max_digits=2),
            preserve_default=False,
        ),
    ]
