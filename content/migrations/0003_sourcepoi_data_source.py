# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_sourcepoi'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcepoi',
            name='data_source',
            field=models.ForeignKey(default=None, to='content.Source'),
            preserve_default=False,
        ),
    ]
