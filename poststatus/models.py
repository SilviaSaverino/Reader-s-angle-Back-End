from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class PostStatus(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    STATUS_CHOICES = (
        ('R', 'Read'),
        ('W', 'Will Read'),
    )
    

    class Meta:
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
