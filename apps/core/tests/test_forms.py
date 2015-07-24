__author__ = 'vitor'
from django.test import TestCase
from apps.core.forms import UsuarioAvaliacaoForm

class AvaliacaoFormTest(TestCase):

    def test_has_fields(self):
        'Form must have 9 fields.'
        form = UsuarioAvaliacaoForm()
        self.assertItemsEqual(['nome', 'email', 'html_c', 'css_c', 'javascript_c', 'python_c', 'django_c',
                               'ios_c', 'android_c'], form.fields)