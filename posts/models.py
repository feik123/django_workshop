from django.core.validators import MinLengthValidator
from django.db import models

from authors.models import Author


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        validators=[MinLengthValidator(5)],
    )

    image_url = models.URLField(

    )

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True
    )

    author = models.ForeignKey(
        to='authors.Author',
        on_delete=models.CASCADE,
        related_name='posts',
    )