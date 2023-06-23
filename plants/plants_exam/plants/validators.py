from django.core.exceptions import ValidationError


def check_name_capital_latter(values):
    if not values[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def plant_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")
