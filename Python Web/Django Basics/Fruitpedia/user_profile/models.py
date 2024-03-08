from django.core.validators import MinLengthValidator
from django.db import models
from django.forms import ValidationError


def validate_username(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[
            MinLengthValidator(2),
            validate_username,
        ],
    )
    last_name = models.CharField(
        max_length=35,
        validators=[
            MinLengthValidator(2),
            validate_username,
        ],
    )
    email = models.EmailField(blank=False, null=False, unique=True)
    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text="*Password length requirements: 8 to 20 characters",
    )
    image_url = models.URLField(blank=True, null=True)
    age = models.PositiveIntegerField(default=18, blank=True, null=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
