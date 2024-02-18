from django.core.validators import MinLengthValidator
from django.db import models
from django.forms import ValidationError


def validate_username(value):
    for char in value:
        if not char.isdigit() and not char.isalpha() and not char == "_":
            raise ValidationError(
                "Ensure this value contains only letters, numbers, and underscore."
            )


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            validate_username,
        ],
    )
    email = models.EmailField()
    age = models.PositiveIntegerField()  # Positive
