from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Post model related to owner/user
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    author = models.TextField(blank=True)
    content = bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_book_w68xtp'
    )
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self)
    return f'{self.id} {self.title}'