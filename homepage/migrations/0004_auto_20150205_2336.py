# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20150205_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
