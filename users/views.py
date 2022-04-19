from rest_framework import viewsets, mixins
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]    
    permission_classes  = [IsAuthenticated, IsAdminUser]
    authentication_classes = [JWTAuthentication]
