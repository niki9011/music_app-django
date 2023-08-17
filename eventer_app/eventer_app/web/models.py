from django.core.validators import MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import EmailValidator


def plant_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False, validators=[plant_name_only_letters])
    last_name = models.CharField(max_length=30, null=False, blank=False, validators=[MinLengthValidator(4)])
    email = models.EmailField(null=False, blank=False, max_length=45)
    profile_picture = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=20, null=False, blank=False, validators=[MinLengthValidator(5)])

    def clean(self):
        if not any(char.isdigit() for char in self.password):
            raise ValidationError("The password must contain at least 1 digit!")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EventModel(models.Model):
    EVENT_CATEGORIES = [
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    ]

    event_name = models.CharField(max_length=30, null=False, blank=False, validators=[MinLengthValidator(2)])
    category = models.CharField(max_length=20, null=False, blank=False, choices=EVENT_CATEGORIES)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    event_image = models.URLField(null=False, blank=False,)

    def clean(self):
        if self.date and self.date < timezone.now().date():
            raise ValidationError("The date cannot be in the past!")

    def __str__(self):
        return self.event_name