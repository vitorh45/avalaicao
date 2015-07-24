__author__ = 'vitor'
from django import forms
from apps.core.models import UsuarioAvaliacao
from apps.core.utils import enviar_email


class UsuarioAvaliacaoForm(forms.ModelForm):

    class Meta:
        model = UsuarioAvaliacao
        fields = ['nome', 'email', 'html_c', 'css_c', 'javascript_c', 'python_c', 'django_c', 'ios_c', 'android_c']

    def save(self, *args, **kwargs):
        # Commit is already set to false
        obj = super(UsuarioAvaliacaoForm, self).save(*args, **kwargs)
        try:
            enviar_email(obj)
        except Exception, e:
            print e
        return obj


