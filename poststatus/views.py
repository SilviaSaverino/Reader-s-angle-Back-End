from rest_framework import generics, permissions
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import PostStatus
from .serializers import PostStatusSerializer


class PostStatusList(generics.ListCreateAPIView):
    """
    API view for listing and creating PostStatus instances.
    """
    serializer_class = PostStatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostStatus.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific PostStatus instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostStatusSerializer
    queryset = PostStatus.objects.all()
