from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'post', 'owner', 'created_at']

    def create(self, validated_data):
        """
        Create a new instance of the serializer's model 
        with the provided data.
        If a duplicate post liked by the user is detected,
        a validation error is raised.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'details': 'post already liked by the user. Possible duplicate'
            })
