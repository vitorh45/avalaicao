#coding: utf-8
from django.db import models
from django.utils import timezone


class UsuarioAvaliacao(models.Model):

    NIVEL_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
    )
    #dados do usuario
    nome = models.CharField('Nome', max_length=150)
    email = models.EmailField('Email')

    #dados da avaliacao

    html_c = models.IntegerField('Conhecimento em HTML', choices= NIVEL_CHOICES, null=True, blank=True)
    css_c = models.IntegerField('Conhecimento em CSS', choices= NIVEL_CHOICES, null=True, blank=True)
    javascript_c = models.IntegerField('Conhecimento em Javascript', choices= NIVEL_CHOICES, null=True, blank=True)
    python_c = models.IntegerField('Conhecimento em Python', choices= NIVEL_CHOICES, null=True, blank=True)
    django_c = models.IntegerField('Conhecimento em Django', choices= NIVEL_CHOICES, null=True, blank=True)
    ios_c = models.IntegerField('Conhecimento em iOS', choices= NIVEL_CHOICES, null=True, blank=True)
    android_c = models.IntegerField('Conhecimento em Android', choices= NIVEL_CHOICES, null=True, blank=True)

    criacao_data = models.DateTimeField(u'Data de criação', default=timezone.now)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name_plural = u'Usuários Avaliações'