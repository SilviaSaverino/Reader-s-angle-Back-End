from rest_framework import serializers
from .models import Post
from post_followers.models import PostFollower


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    following_id = serializers.SerializerMethodField()
    
    
    def validate_image(self, value):
        """
        Validate the size and dimensions of the image field
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Get whether the authenticated user is the owner of the post
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Retrieve the ID of the post follower, if the authenticated user follows the post.
        If the user is not authenticated or doesn't follow the post, return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = PostFollower.objects.filter(
                owner=user, followed_post=obj.id
            ).first()
            return following.id if following else None
        return None        
            
    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'profile_id', 'profile_image', 'created_at', 'updated_at', 'title',
            'author', 'content', 'image', 'is_owner', 'genre_filter', 'image_filter', 'following_id',
        ]
