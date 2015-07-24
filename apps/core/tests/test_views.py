from django.test import TestCase
from django.core.urlresolvers import reverse as r
from django.core import mail
from apps.core.forms import UsuarioAvaliacaoForm
from apps.core.models import UsuarioAvaliacao


class AvaliacaoViewTest(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('index'))

    def test_get(self):
        #get / deve retornar status code 200
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        #template renderizado deve ser o index.html
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_has_form_on_context(self):
        #se o form esta no contexto
        self.assertIsInstance(self.resp.context['form'], UsuarioAvaliacaoForm)

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 3)
        self.assertContains(self.resp, '<select', 7)


class AvaliacaoViewPostTest(TestCase):

    def setUp(self):
        data = {'nome': 'Vitor Hugo Campos', 'email': 'vitorh45@gmail.com'}
        self.resp = self.client.post(r('index'), data)

    def test_post(self):
        #post / deve retornar status code 200
        self.assertEqual(200, self.resp.status_code)

    def test_save(self):
        #se salvou o registro
        self.assertTrue(UsuarioAvaliacao.objects.exists())

    def test_send_email(self):
        self.assertEqual(len(mail.outbox), 1)

class AvaliacaoViewInvalidPostTest(TestCase):

    def setUp(self):
        data = {'nome':'vitor hugo campos'}
        self.resp = self.client.post(r('index'), data)

    def test_post(self):
        #post / deve retornar status code 200
        self.assertEqual(200, self.resp.status_code)

    def test_form_error(self):
        #se o form retornou erro
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        #se nao salvou o registro
        self.assertFalse(UsuarioAvaliacao.objects.exists())