from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ProfileModel(models.Model):
    email = models.EmailField(null=False, blank=False,)
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(12)])
    password = models.CharField(null=False, blank=False,max_length=30,)
    first_name = models.CharField(null=True, blank=True,max_length=30,)
    last_name = models.CharField(null=True, blank=True,max_length=30,)
    profile_picture = models.URLField(null=True, blank=True,)


class GameModel(models.Model):

    CHOICES = (("Action", "Action"), ("Adventure", "Adventure"),
              ("Puzzle", "Puzzle"), ("Strategy", "Strategy"),
              ("Board/Card Game", "Board/Card Game"), ("Other", "Other"),)

    title = models.CharField(max_length=30, null=False, blank=False, unique=True,)
    category = models.CharField(max_length=15, choices=CHOICES,)
    rating = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.1), MaxValueValidator(5.0)])
    max_level = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)],)
    image_url = models.URLField(null=False, blank=False)
    summary = models.TextField(null=True, blank=True,)
