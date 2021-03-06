# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0002_user_hire_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('join', models.ManyToManyField(related_name='Users', to='loginreg.User')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginreg.User')),
            ],
        ),
    ]
