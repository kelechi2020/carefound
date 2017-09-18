# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atiku', '0007_auto_20170917_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantinfo',
            name='landmark_identity',
            field=models.CharField(max_length=400, blank=True, verbose_name='Landmark'),
        ),
    ]
