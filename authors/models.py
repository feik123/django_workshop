from django.core.validators import MinLengthValidator
from django.db import models

from authors.validators import AlphabeticValidator, NumberLengthValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            AlphabeticValidator(),
        ],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            AlphabeticValidator(),
        ]
    )

    passcode = models.CharField(
        help_text="Your passcode must be a combination of 6 digits",
        max_length=6,

        validators=[
            MinLengthValidator(6),
            NumberLengthValidator()
        ]
    )

    pets_number = models.PositiveSmallIntegerField(

    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )