from .models import PostIt
from .serializers import PostItSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostItList(APIView):
    def get(self, request):
        postits = PostIt.objects.all()
        serializer = PostItSerializer(postits, many=True)
        return Response(serializer.data)

class PostItViewSet(viewsets.ModelViewSet):
    queryset = PostIt.objects.all()
    serializer_class = PostItSerializer
    permission_classes  = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
