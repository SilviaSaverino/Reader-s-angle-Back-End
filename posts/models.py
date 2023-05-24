from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model related to owner/user
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    genre_filter_choices = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('mystery', 'Mystery'),
        ('fantasy', 'Fantasy'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('biography', 'Biography'),
        ('poetry', 'Poetry'),
        ('children', 'Children'),
        ('cookbooks', 'Cookbooks')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        error_messages={
            "unique": "A post with this title already exists. Possible duplicate"})
    author = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_book_w68xtp'
    )
    image_filter = models.CharField(
        max_length=30, choices=image_filter_choices, default='normal')
    genre_filter = models.CharField(
        max_length=30, choices=genre_filter_choices, default='normal')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
