# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioavaliacao',
            name='criacao_data',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de cria\xe7\xe3o'),
        ),
    ]
