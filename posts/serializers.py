from rest_framework import serializers
from post_followers.models import PostFollower
from likes.models import Like
from poststatus.models import PostStatus
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    following_id = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    review_count = serializers.ReadOnlyField()
    followed_count = serializers.ReadOnlyField()
    post_status = serializers.SerializerMethodField()

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
        Retrieve the ID of the post follower, 
        if the authenticated user follows the post.
        If the user is not authenticated or 
        doesn't follow the post, return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = PostFollower.objects.filter(
                owner=user, followed_post=obj.id
            ).first()
            return following.id if following else None
        return None        

    def get_like_id(self, obj):
        """
        Retrieve the ID of the like associated with the post,
        if the authenticated user has liked the post.
        If the user is not authenticated or 
        hasn't liked the post, return None.
        """     
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_post_status(self, obj):
        """
        Retrieve the status of the post for the authenticated user.
        If the user is not authenticated or no status is found, return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            post_status = PostStatus.objects.filter(owner=user, post=obj).first()
            return post_status.status if post_status else None
        return None


    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title',
            'author', 'content', 'image', 'is_owner',
            'genre_filter', 'image_filter', 'following_id','like_id',
            'likes_count', 'review_count', 'followed_count',
            'post_status',
        ]
