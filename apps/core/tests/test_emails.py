__author__ = 'vitor'
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from django.core import mail


class AvaliacaoEmailTest(TestCase):

    def test_receive_front_end_email(self):
        data = {'nome': 'Vitor Hugo Campos', 'email': 'vitorh45@gmail.com', 'html_c':8, 'css_c':9, 'javascript_c':10}
        resp = self.client.post(r('index'), data)
        self.assertEqual(200, resp.status_code)
        self.assertIn('Front End', mail.outbox[0].body)

    def test_receive_back_end_email(self):
        data = {'nome': 'Vitor Hugo Campos', 'email': 'vitorh45@gmail.com', 'python_c':8, 'django_c':9}
        resp = self.client.post(r('index'), data)
        self.assertEqual(200, resp.status_code)
        self.assertIn('Back End', mail.outbox[0].body)

    def test_receive_mobile_email(self):
        data = {'nome': 'Vitor Hugo Campos', 'email': 'vitorh45@gmail.com', 'ios_c':8, 'android_c':9}
        resp = self.client.post(r('index'), data)
        self.assertEqual(200, resp.status_code)
        self.assertIn('Mobile', mail.outbox[0].body)

    def test_receive_3_emails(self):
        data = {'nome': 'Vitor Hugo Campos', 'email': 'vitorh45@gmail.com', 'html_c':8, 'css_c':9, 'javascript_c':10,
                'python_c':8, 'django_c':9, 'ios_c':8, 'android_c':9}
        resp = self.client.post(r('index'), data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(3, len(mail.outbox))