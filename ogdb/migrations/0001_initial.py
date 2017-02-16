# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 16:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_lastname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('person_firstname', models.CharField(max_length=20, verbose_name='First Name')),
                ('person_title', models.CharField(choices=[('TI', 'Technical Intern'), ('NTI', 'Non-Technical Intern'), ('SUP', 'Supervisior'), ('DON', 'Donor'), ('FTE', 'Full-Time Employee'), ('NA', 'N/A')], max_length=19)),
                ('person_date', models.DateField(default=datetime.date.today, verbose_name='Start Date')),
            ],
        ),
    ]