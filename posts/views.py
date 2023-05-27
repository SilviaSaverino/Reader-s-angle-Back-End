from django.db.models import Count
from rest_framework import  permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post 
    with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        review_count=Count('review', distinct=True),
        followed_count=Count('followed', distinct=True),
       
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
          
    ]
    
    ordering_fields = [
        'likes_count',
        'review_count',
        'followed_count',
        'likes__created_at',
        
    ]
    search_fields = [
        'owner__username',
        'title',
        'genre_filter',
        'author', 
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if the 
    current user owns it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        review_count=Count('review', distinct=True),
        followed_count=Count('followed', distinct=True),
    ).order_by('-created_at')

