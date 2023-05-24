from django.urls import path
from reviewlikes import views

urlpatterns = [
    path('reviewlikes/', views.ReviewLikeList.as_view()),
    path('reviewlikes/<int:pk>', views.ReviewLikeDetail.as_view())
]

