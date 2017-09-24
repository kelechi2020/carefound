# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atiku', '0003_auto_20170921_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localgovernment',
            name='name',
            field=models.CharField(max_length=300, db_index=True),
        ),
    ]
