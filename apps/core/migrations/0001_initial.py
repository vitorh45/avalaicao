# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioAvaliacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('html_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em HTML', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
                ('css_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em CSS', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
                ('javascript_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em Javascript', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
                ('python_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em Python', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
                ('django_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em Django', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
                ('ios_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em iOS', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
                ('android_c', models.IntegerField(default=0, null=True, verbose_name=b'Conhecimento em Android', blank=True, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9')])),
            ],
        ),
    ]
