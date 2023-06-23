from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_name_capital_latter, plant_name_only_letters


class ProfileModel(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2)],
    )

    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[check_name_capital_latter],
    )

    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[check_name_capital_latter],
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def ful_name(self):
        return f"{self.first_name}{self.last_name}"


class Plant(models.Model):
    CHOISES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    plan_type = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        choices=CHOISES
    )

    name = models.CharField(
        max_length=20,
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

    price = models.FloatField(
        null=False,
        blank=False,
    )