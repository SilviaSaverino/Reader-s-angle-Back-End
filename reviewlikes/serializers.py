from django.db import IntegrityError
from rest_framework import serializers
from .models import ReviewLike


class ReviewLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the ReviewLike model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ReviewLike
        fields = ['id', 'review', 'owner', 'created_at']

    def create(self, validated_data):
        """
        Create a new instance of the serializer's model 
        with the provided data.
        If a duplicate review liked by the user is detected,
        a validation error is raised.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'details': 'Review already liked by the user. Possible duplicate'
            })
