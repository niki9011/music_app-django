from django.core.exceptions import ValidationError


def check_name_only_letters(values):
    if not values[0].isalpha():
        raise ValidationError("Your name must start with a capital letter!")


def plant_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")