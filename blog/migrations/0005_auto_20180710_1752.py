# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-10 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
