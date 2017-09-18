# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atiku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantinfo',
            name='mothers_maiden_name',
            field=models.CharField(verbose_name='Mothers Maiden Name', max_length=40),
        ),
    ]
