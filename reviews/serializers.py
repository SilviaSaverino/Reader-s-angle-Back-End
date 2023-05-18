from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Reviews model.
    Add extra fields when returning a list of reviews
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    
    def get_is_owner(self, obj):
        """
        Get whether the authenticated user is the owner of the review
        """
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'post', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'content', 'is_owner',
        ]
        

class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in Detail view
    The edited review will be associated to the same post.
    """
    post = serializers.ReadOnlyField(source='post.id')