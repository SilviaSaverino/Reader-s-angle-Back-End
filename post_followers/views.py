from rest_framework import generics, permissions
from readersandle_api.permissions import IsOwnerOrReadOnly 
from .models import PostFollower
from .serializers import PostFollowerSerializer

class PostFollowerList(generics.ListCreateAPIView):
    """
    List all post followers.
    Create a post follower, i.e., follow a post if logged in.
    Perform_create: associate the current logged-in user with a post follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostFollower.objects.all()
    serializer_class = PostFollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostFollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a post follower.
    No update view, as we either follow or unfollow posts.
    Destroy a post follower, i.e., unfollow a post if the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = PostFollower.objects.all()
    serializer_class = PostFollowerSerializer