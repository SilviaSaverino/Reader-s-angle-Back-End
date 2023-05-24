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

    def create(self, validated_data):
        """
        Create a new instance of the serializer's model.
        If a duplicate status for the post and user is detected,
        the existing instance is updated instead of creating a new one.
        """
        post = validated_data['post']
        owner = validated_data['owner']
        status = validated_data['status']

        existing_instance = PostStatus.objects.filter(post=post, owner=owner).first()

        if existing_instance:
            existing_instance.status = status
            existing_instance.save()
            return existing_instance

        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'details': 'An error occurred while creating the post status.'
            })
