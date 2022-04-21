from django.urls import path, include
from .views import UserCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserCreateView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
