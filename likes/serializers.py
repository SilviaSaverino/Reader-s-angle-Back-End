from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    """
    owner = serializer.ReadOnlyField(source='owner.username')
    
    
    class Mera:
        model = Like
        fields = ['id', 'post', 'owner', 'created_at']