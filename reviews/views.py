from rest_framework import generics, permissions, filters
from django.db.models import Count
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


class ReviewList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating reviews.
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.annotate(
        reviewlikes_count=Count(
            'reviewlike', distinct=True
        )
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'reviewlikes_count',
    ]

    def perform_create(self, serializer):
        """Allows to perform additional actions or 
        modifications before saving the instance.
        """
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a review by its
    id if the current user owns it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ReviewDetailSerializer
    queryset = Review.objects.all()
