# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuarioavaliacao_criacao_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarioavaliacao',
            options={'verbose_name_plural': 'Usu\xe1rios Avalia\xe7\xf5es'},
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='android_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em Android', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='css_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em CSS', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='django_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em Django', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='html_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em HTML', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='ios_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em iOS', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='javascript_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em Javascript', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
        migrations.AlterField(
            model_name='usuarioavaliacao',
            name='python_c',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Conhecimento em Python', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')]),
        ),
    ]
