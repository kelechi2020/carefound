# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='First Name', max_length=40)),
                ('last_name', models.CharField(verbose_name='Surname', max_length=40)),
                ('mothers_maiden_name', models.CharField(verbose_name='First Name', max_length=40)),
                ('address', models.CharField(verbose_name='Address', max_length=100)),
                ('state', models.CharField(verbose_name='State', max_length=100)),
                ('local_government', models.CharField(verbose_name='Local Government', max_length=70)),
                ('district', models.CharField(verbose_name='District', blank=True, max_length=600)),
                ('landmark_identity', models.CharField(verbose_name='Landmark', max_length=400)),
                ('phone_number', models.IntegerField(verbose_name='Phone Number')),
                ('email', models.EmailField(verbose_name='E-mail', max_length=100)),
                ('communication_means1', models.BooleanField(verbose_name='Ist Means Of Communication')),
                ('communication_means2', models.BooleanField(verbose_name='Second Means Of Communication')),
            ],
        ),
    ]
