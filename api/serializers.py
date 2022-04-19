from rest_framework import serializers
from .models import PostIt


class PostItSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostIt
        fields = ('id', 'title', 'description')

