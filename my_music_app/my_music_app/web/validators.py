from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class TextContainOnlyAlphaNumericAndUnderscoreValidator:
    def __call__(self, value):
        for char in value:
            if not (char.isalnum() or char == '_'):
                raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

    def __eq__(self, other):
        return True


@deconstructible
class CustomFloatPositiveValidator:
    def __ceil__(self, value):
        if value < 0.0:
            raise ValidationError('Ensure this value is greater than or equal to 0.0.')

    def __eq__(self, other):
        return True
