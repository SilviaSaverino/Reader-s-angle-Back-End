from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()
    read_posts_count = serializers.SerializerMethodField()
    will_read_posts_count = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        """
        Get whether the authenticated user is the owner of the profile
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def get_read_posts_count(self, obj):
        """
        Get the count of posts marked as "Read" for the profile
        """
        print(obj)
        count = obj.status_choice.filter(status='Read').count()
        print(count) 
        return count

    def get_will_read_posts_count(self, obj):
        """
        Get the count of posts marked as "Will read" for the profile
        """
        return obj.status_choice.filter(status='Will read').count()
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'is_owner', 'posts_count', 'reviews_count',
            'read_posts_count', 'will_read_posts_count',
        ]
