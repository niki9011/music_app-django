from django.db import models
from django.core.validators import MinLengthValidator
from .validators import TextContainOnlyAlphaNumericAndUnderscoreValidator,\
    CustomFloatPositiveValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2),
                    TextContainOnlyAlphaNumericAndUnderscoreValidator,
                    ]
    )

    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


class Album(models.Model):
    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRE_CHOICES = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER, OTHER),)

    album_name = models.CharField(
        blank=False, null=False, unique=True, max_length=30, verbose_name='Album Name'
    )
    artist = models.CharField(
        blank=False, null=False, max_length=30
    )
    genre = models.CharField(
        max_length=30, choices=GENRE_CHOICES, blank=False, null=False,
    )
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, verbose_name='Image URL')
    price = models.FloatField(
        blank=False, null=False, validators=[CustomFloatPositiveValidator]
    )

    class Meta:
        ordering = ('id',)


profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
