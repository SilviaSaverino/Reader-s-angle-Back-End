from rest_framework import generics, permissions
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import PostFollower
from .serializers import PostFollowerSerializer


class PostFollowerList(generics.ListCreateAPIView):
    """
    View for listing and creating PostFollower instances.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostFollower.objects.all()
    serializer_class = PostFollowerSerializer

    # def get_queryset(self):
    #     return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostFollowerDetail(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting a specific PostFollower instance.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PostFollower.objects.all()
    serializer_class = PostFollowerSerializer
