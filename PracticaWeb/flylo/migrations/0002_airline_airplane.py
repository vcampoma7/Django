# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-24 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flylo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40)),
                ('reference_code', models.CharField(max_length=100)),
                ('number_seats_tourist', models.CharField(max_length=5)),
                ('number_seats_business', models.CharField(max_length=5)),
                ('number_seats_excellence', models.CharField(max_length=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flylo.Airline')),
            ],
        ),
    ]
