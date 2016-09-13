# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ca', '0010_auto_20160912_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorDetail', models.TextField()),
                ('dd', models.BooleanField(default=False)),
                ('studentBodyDetail', models.TextField()),
                ('sbd', models.BooleanField(default=False)),
                ('ca', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ca.CAProfile')),
            ],
        ),
    ]