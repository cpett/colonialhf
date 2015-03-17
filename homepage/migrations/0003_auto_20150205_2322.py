# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
