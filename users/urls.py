from django.urls import path, include
from .views import UserViewSet, UserCreateView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserCreateView, basename='users')
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]
