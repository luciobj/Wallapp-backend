from django.urls import path, include
from .views import PostItViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('postit', PostItViewSet, basename='postit')


urlpatterns = [
    path('', include(router.urls)),
]
