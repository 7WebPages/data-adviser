# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=2048, unique=True)),
                ('parent_category', models.ForeignKey(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='provider',
            field=models.ForeignKey(to='core.Provider'),
        ),
    ]
