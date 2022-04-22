import pytest
from rest_framework.test import APITestCase
from ..models import PostIt


pytestmark = pytest.mark.django_db

test_postit = {
    "title": "Test",
    "description": "This is a test Post It",
}

class PostitModelTests(APITestCase):
    def test_postit(self):
        postit_quantity = PostIt.objects.all().count()
        postit, bool = PostIt.objects.get_or_create(test_postit)
        assert postit.title == test_postit['title']
        assert postit.description == test_postit['description']
        assert PostIt.objects.all().count() == postit_quantity + 1
