# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wwidmer', '0003_project_introimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='introImage',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
