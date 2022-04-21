from django.urls import path
from .views import UserCreateView


urlpatterns = [
    path('users/', UserCreateView.as_view({'post': 'create'}), name='user-create'),
]
