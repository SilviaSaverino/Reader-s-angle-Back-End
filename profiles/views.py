from rest_framework import generics, filters
from django.db.models import Count, Case, When
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
        reviews_count = Count('owner__review', distinct=True),
        read_posts_count=Count(Case(When(status_choice__status='Read', then=1))),
        will_read_posts_count=Count(Case(When(status_choice__status='Will read', then=1))),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends= [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'reviews_count',
        'read_posts_count',
        'will_read_posts_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if the current user
    is the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = Profile.objects.all()
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        reviews_count=Count('owner__review', distinct=True),
        # read_posts_count=Count('owner__status_choice', filter=Case(When(owner__status_choice__status='Read', then=1)), distinct=True),
        # will_read_posts_count=Count('owner__status_choice', filter=Case(When(owner__status_choice__status='Will read', then=1)), distinct=True),
    ).all()
    serializer_class = ProfileSerializer
