# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourcePoi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
