import pytest
from rest_framework.test import APITestCase
from django.urls import resolve, reverse


pytestmark = pytest.mark.django_db

user = {
    "username": 'test',
    "email": 'test@email.com',
    "password": '123456',
    "password2": '123456',
}

class TestUserListView(APITestCase):
    def test_reverse_resolve(self):
        assert reverse("user-create") == "/users/"
        assert resolve("/users/").view_name == "user-create"

    def test_status_code(self):
        url = reverse("user-create")
        response = self.client.post(url, user, format="json")
        assert response.status_code == 201
