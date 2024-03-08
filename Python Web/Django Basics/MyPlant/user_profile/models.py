from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_name_capital(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    first_name = models.CharField(max_length=20, validators=[validate_name_capital])
    last_name = models.CharField(max_length=20, validators=[validate_name_capital])
    picture = models.URLField(blank=True, null=True)
