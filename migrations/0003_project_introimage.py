# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wwidmer', '0002_auto_20141126_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='introImage',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
