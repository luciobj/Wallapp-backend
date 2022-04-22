from pydoc import describe
from turtle import update
import pytest
from rest_framework.test import APITestCase
from django.urls import resolve, reverse


pytestmark = pytest.mark.django_db

test_user = {
    "username": "test",
    "email": "test@test.com",
    "password": "123456",
    "password2": "123456",
}

test_postit = {
    "title": "Testing",
    "description": "This is a test in progress Post It",
}

updated_postit = {
    "title": "Updated testing",
    "description": "This is an updated test in progress Post It",
}

class TestPostItListView(APITestCase):
    def login(self):
        url = reverse("user-create")
        response = self.client.post(url, test_user, format="json")
        assert response.status_code == 201
        url = reverse("auth")
        login_credentials = {
            "username": test_user['username'],
            "password": test_user['password'],
        }
        response = self.client.post(url, login_credentials, format="json")
        assert response.status_code == 200
        return response.data['token']

    def test_resolve_reverse(self):
        assert reverse("get-list") == "/api/get/"
        assert resolve("/api/get/").view_name == "get-list"
        assert reverse("postit-list") == "/api/postit/"

    def test_list_view(self):
        url = reverse("get-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_crud_functions(self):
        login = self.login()
        url = reverse("postit-list")
        response = self.client.post(url, test_postit, format="json", 
            HTTP_AUTHORIZATION='Token ' + login)
        assert response.status_code == 201

        id = response.data['id']
        postit_url = reverse("postit-detail", args=[id])
        response = self.client.put(postit_url, updated_postit, format="json", HTTP_AUTHORIZATION='Token ' + login)
        assert response.status_code == 200
        assert response.data['title'] == updated_postit['title']
        assert response.data['description'] == updated_postit['description']

        response = self.client.delete(postit_url, format="json", HTTP_AUTHORIZATION='Token ' + login)
        assert response.status_code == 204
