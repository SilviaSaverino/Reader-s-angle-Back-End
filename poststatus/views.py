from rest_framework import generics, permissions
from readersandle_api.permissions import IsOwnerOrReadOnly
from .models import PostStatus
from .serializers import PostStatusSerializer


class PostStatusList(generics.ListCreateAPIView):
   
    serializer_class = PostStatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostStatus.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostStatusSerializer
    queryset = PostStatus.objects.all()
