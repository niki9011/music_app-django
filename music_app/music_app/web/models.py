from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from .validators import validate_only_alphanumeric


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=[MinLengthValidator(2), validate_only_alphanumeric],
    )

    email = models.EmailField(null=False, blank=False,)

    age = models.PositiveIntegerField(null=True, blank=True,)


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=MUSICS
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0.0)]
    )
