from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
        )
    stars = models.IntegerField(
        validators =[
            MinValueValidator(0, "Rating must be at least 0 stars"),
            MaxValueValidator(5, "Rating must be at most 5 stars")
        ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.stars} stars for {self.movie.title}'
