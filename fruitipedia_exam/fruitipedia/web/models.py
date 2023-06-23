from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_name_only_letters, plant_name_only_letters


class Profile(models.Model):

    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), check_name_only_letters],
    )

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=[MinLengthValidator(1), check_name_only_letters],
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,

    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[MinLengthValidator(8)],

    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(null=True, blank=True, default=18)

    # def ful_name(self):
    #     return f"{self.first_name}{self.last_name}"


class Fruit(models.Model):

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), plant_name_only_letters]

    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
