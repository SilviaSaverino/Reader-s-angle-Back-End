from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class PostFollower(models.Model):
    """
    Model to represent the followers of posts.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f'{self.user.username} follows post {self.post.id}'
