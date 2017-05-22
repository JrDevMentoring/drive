# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Suggestion',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('suggestion_text', models.CharField(max_length=500)),
        ('votes', models.IntegerField(default=0)),
        ('pub_date', models.DateTimeField(verbose_name='date published')),
      ],
    ),
  ]