from rest_framework import generics, filters
from django.db.models import Count
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    Profile creation is handled by Django signals
    """
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        reviews_count = Count('owner__review', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends= [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'reviews_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if the current user
    is the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
