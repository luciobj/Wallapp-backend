from django.urls import path, include
from .views import PostItViewSet, PostItList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('get', PostItList, basename='get')
router.register('postit', PostItViewSet, basename='postit')


urlpatterns = [
    path('api/', include(router.urls)),
]
