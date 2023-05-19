from django.db import IntegrityError
from rest_framework import serializers
from .models import PostStatus


class PostStatusSerializer(serializers.ModelSerializer):
    """
    Serializer for the PostStatus model
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    
    class Meta:
        model = PostStatus
        fields = ['id', 'post', 'owner', 'status']