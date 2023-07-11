from django.core import exceptions
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_years(value):
    min_year = 1980
    max_year = 2049
    if not min_year <= value <= max_year:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(18)],
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,)

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True, )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    CHOICES = (("Sports Car", "Sports Car" ),
               ("Pickup", "Pickup"),
               ("Crossover", "Crossover"),
               ("Minibus", "Minibus"),
               ("Other", "Other"))

    type = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=CHOICES
    )

    model = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[MinLengthValidator(2)],
    )

    year = models.IntegerField(
        null=True,
        blank=True,
        validators=[validate_years]
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
    )
