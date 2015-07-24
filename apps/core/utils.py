__author__ = 'vitor'
from django.conf import settings
from django.core.mail import send_mail
from collections import defaultdict
import string

def enviar_email(obj):
        email_assunto = settings.EMAIL_SUBJECT
        habilidades = get_usuario_habilidades(obj)
        if habilidades:
            for habilidade in habilidades:
                mensagem = get_mensagem(habilidade=habilidade)
                send_mail(email_assunto, mensagem, settings.EMAIL_HOST_USER, [obj.email,])
        else:
            mensagem = get_mensagem()
            send_mail(email_assunto, mensagem, settings.EMAIL_HOST_USER, [obj.email,])


def get_usuario_habilidades(obj):
    habilidades = []
    if obj.html_c > 6 and obj.css_c > 6 and obj.javascript_c > 6:
        habilidades.append('Front End ')
    if obj.python_c > 6 and obj.django_c > 6:
        habilidades.append('Back End ')
    if obj.ios_c > 6 and obj.android_c > 6:
        habilidades.append('Mobile ')
    return habilidades

def get_mensagem(**kwargs):

    return string.Formatter().vformat(settings.EMAIL_MESSAGE, (), defaultdict(str, **kwargs))