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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Surname')),
                ('mothers_maiden_name', models.CharField(max_length=40, blank=True, verbose_name='Mothers Maiden Name')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('state', models.CharField(max_length=100, choices=[('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWAIBOM', 'AKWAIBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSSRIVERS', 'CROSSRIVERS'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')], verbose_name='State')),
                ('local_government', models.CharField(max_length=70, verbose_name='Local Government')),
                ('sex', models.CharField(max_length=10, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], verbose_name='Sex')),
                ('district', models.CharField(max_length=600, blank=True, verbose_name='District')),
                ('landmark_identity', models.CharField(max_length=400, blank=True, verbose_name='Landmark')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('communication_means1', models.NullBooleanField(verbose_name='Ist Means Of Communication')),
                ('communication_means2', models.NullBooleanField(verbose_name='Second Means Of Communication')),
            ],
        ),
        migrations.CreateModel(
            name='LocalGovernment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='localgovernment',
            name='country',
            field=models.ForeignKey(to='atiku.State'),
        ),
    ]
