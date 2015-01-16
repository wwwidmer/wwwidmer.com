# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wwidmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='content',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='short',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.CharField(default=' ', max_length=500, blank=True),
            preserve_default=False,
        ),
    ]
