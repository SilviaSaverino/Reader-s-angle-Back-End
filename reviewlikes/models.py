from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review


class ReviewLike(models.Model):
    """
    ReviwLike model, related to 'owner' and 'review'.
    It represents the likes for the reviews.
    'unique_together' makes sure a user can't like the same review twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'review']

    def __str__(self):
        return f'{self.owner} liked the review {self.review}'
