# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atiku', '0008_auto_20170917_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantinfo',
            name='communication_means1',
            field=models.NullBooleanField(verbose_name='Ist Means Of Communication'),
        ),
        migrations.AlterField(
            model_name='applicantinfo',
            name='communication_means2',
            field=models.NullBooleanField(verbose_name='Second Means Of Communication'),
        ),
    ]
