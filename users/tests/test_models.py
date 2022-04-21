import pytest
from rest_framework.test import APITestCase
from ..models import User
from django.core import mail
from django.test import TestCase

pytestmark = pytest.mark.django_db

class UserModelTests(APITestCase):
    def test_create_user(self):
        user_quantity = User.objects.all().count()
        user = User.objects.create_user(
            username="test", email="test@email.com", password="123456"
        )
        assert user.username == "test"
        assert user.email == "test@email.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
        assert User.objects.all().count() == user_quantity + 1

    def test_create_superuser(self):
        user_quantity = User.objects.all().count()
        user = User.objects.create_superuser(
            username="admin", email="admin@email.com", password="123456"
        )
        assert user.username == "admin"
        assert user.email == "admin@email.com"
        assert user.is_active
        assert user.is_staff
        assert user.is_superuser
        assert User.objects.all().count() == user_quantity + 1


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail(
            'Welcome to WallApp',
            'You have been registered',
            'wallapp-not-reply@hotmail.com',
            ['test@test.com'],
            fail_silently=False,
        )

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Welcome to WallApp')
