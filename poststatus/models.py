from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile

class PostStatus(models.Model):
    """
    Model to represent the status of a post for a user.
    """
    STATUS_CHOICES = (
        ('Read', 'Read'),
        ('Will read', 'Will Read'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='poststatus', on_delete=models.CASCADE
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='status_choice', default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        """
        Return a string representation of the PostStatus instance.
        """
        return f'{self.owner} {self.post}'
