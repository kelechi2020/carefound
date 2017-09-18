# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atiku', '0004_auto_20170915_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantinfo',
            name='phone_number',
            field=models.CharField(max_length=30, verbose_name='Phone Number'),
        ),
    ]
