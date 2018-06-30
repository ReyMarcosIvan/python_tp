# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('comienzo', models.DateTimeField(default=django.utils.timezone.now)),
                ('fin', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trabajo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('lugar', models.CharField(max_length=200)),
                ('comienzo', models.DateTimeField(default=django.utils.timezone.now)),
                ('fin', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Intereses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interes', models.CharField(max_length=200)),
                ('icono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Redes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.CharField(max_length=200)),
                ('icono', models.CharField(max_length=200)),
            ],
        ),
    ]
