from django.urls import path
from poststatus.views import PostStatusList, PostStatusDetail

urlpatterns = [
    path('poststatus/', PostStatusList.as_view(), name='poststatus-list'),
    path('poststatus/<int:pk>/', PostStatusDetail.as_view(), name='poststatus-detail'),
]