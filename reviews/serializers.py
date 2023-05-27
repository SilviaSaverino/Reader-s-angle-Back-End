from rest_framework import serializers
from reviewlikes.models import ReviewLike
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
    reviewlike_id = serializers.SerializerMethodField()
    reviewlikes_count =  serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Get whether the authenticated user is the owner of the review
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_reviewlike_id(self, obj):
        """
        Retrieve the ID of the like associated with the review,
        if the authenticated user has liked the review.
        If the user is not authenticated or 
        hasn't liked the review, return None.
        """     
        user = self.context['request'].user
        if user.is_authenticated:
            reviewlike = ReviewLike.objects.filter(
                owner=user, review=obj
            ).first()
            return reviewlike.id if reviewlike else None
        return None
    
    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'post', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'content', 'is_owner', 'reviewlike_id',
            'reviewlikes_count',
        ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in Detail view
    The edited review will be associated to the same post.
    """
    post = serializers.ReadOnlyField(source='post.id')
