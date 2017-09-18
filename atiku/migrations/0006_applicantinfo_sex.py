# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('atiku', '0005_auto_20170916_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantinfo',
            name='sex',
            field=models.CharField(max_length=10, verbose_name='Sex', default=datetime.datetime(2017, 9, 17, 0, 58, 33, 782916, tzinfo=utc), choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')]),
            preserve_default=False,
        ),
    ]
