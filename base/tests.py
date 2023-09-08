from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import mail
from .models import VerifyModel


# Create your tests here.
class TestBase(TestCase):
    def test_base(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class TestLogin(TestCase):
    def test_login_get(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        User.objects.create_user(username='paprut539@gmail.com', password='31rasune', first_name='Pavel',
                                 last_name='Prokopev')
        response = self.client.post('/login', data={'email': 'paprut539@gmail.com', 'password': '31rasune'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/login', data={'email': 'dds@gmail.com', 'password': '31rasune'})
        self.assertEqual(response.context[0].dicts[3]['message'], 'Incorrect email or password')


class TestRegistration(TestCase):
    def test_registration_get(self):
        response = self.client.get('/registration')
        self.assertEqual(response.status_code, 200)

    def test_message(self):
        res = mail.send_mail('hello_0', 'hello_1', '0@example.com', ['1@example.com'])
        self.assertEqual(mail.outbox[0].to[0], '1@example.com')
        self.assertEqual(mail.outbox[0].from_email, '0@example.com')
        self.assertEqual(mail.outbox[0].body, 'hello_1')


    def test_verify(self):
        VerifyModel.objects.create(username='1', password='2', first_name='3', last_name='4', code='1234')
        response = self.client.post('/registration', data={'stage': 'verify', 'user_code': '1234', 'username': '1'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/registration', data={'stage': 'verify', 'user_code': '4321', 'username': '1'})
        self.assertEqual(response.context[0].dicts[3]['message'], 'Invalid code')

