# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='meta_description',
            field=models.TextField(help_text='The text displayed in search engines.', max_length=320, null=True, verbose_name='description', blank=True),
        ),
    ]
