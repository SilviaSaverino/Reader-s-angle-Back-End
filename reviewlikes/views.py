from rest_framework import generics, permissions
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import ReviewLike
from .serializers import ReviewLikeSerializer


class ReviewLikeList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating review likes.
    """
    serializer_class = ReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ReviewLike.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReviewLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or destroy a like by its id. 
    A user is able to like a review
    only if is logged in.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewLikeSerializer
    queryset = ReviewLike.objects.all()