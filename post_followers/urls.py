from django.urls import path
from post_followers import views

urlpatterns = [
    path('post_followers/', views.PostFollowerList.as_view()),
    path('post_followers/<int:pk>/', views.PostFollowerDetail.as_view())
]
