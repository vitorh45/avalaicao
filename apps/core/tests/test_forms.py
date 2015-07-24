__author__ = 'vitor'
from django.test import TestCase
from apps.core.forms import UsuarioAvaliacaoForm

class AvaliacaoFormTest(TestCase):

    def test_has_fields(self):
        #form deve conter 9 campos
        form = UsuarioAvaliacaoForm()
        self.assertItemsEqual(['nome', 'email', 'html_c', 'css_c', 'javascript_c', 'python_c', 'django_c',
                               'ios_c', 'android_c'], form.fields)

    def test_email_valid(self):
        #campo email deve conter email valido
        data = {'nome': 'vitor hugo campos', 'email': 'vitorgmail'}
        form = UsuarioAvaliacaoForm(data)
        form.is_valid()
        self.assertItemsEqual(['email'], form.errors)