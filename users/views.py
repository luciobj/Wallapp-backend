from rest_framework import viewsets, mixins
from .models import User
from .serializers import UserSerializer
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response


class UserCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            send_mail(
                'Welcome to WallApp',
                'You have been registered',
                'wallapp-not-reply@hotmail.com',
                [request.data['email']],
                fail_silently=True,
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
