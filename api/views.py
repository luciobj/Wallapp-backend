from .models import PostIt
from .serializers import PostItSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostItList(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer

class PostItViewSet(viewsets.ModelViewSet):
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer
    permission_classes  = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
