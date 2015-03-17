# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.TextField(max_length=75, null=True, blank=True)),
                ('address', models.TextField(max_length=100, null=True, blank=True)),
                ('city', models.TextField(max_length=50, null=True, blank=True)),
                ('state', models.TextField(max_length=2, null=True, blank=True)),
                ('zip', models.IntegerField(null=True, blank=True)),
                ('event', models.ForeignKey(blank=True, null=True, to='homepage.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
