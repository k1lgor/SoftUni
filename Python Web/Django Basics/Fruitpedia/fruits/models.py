from django.core.validators import MinLengthValidator
from django.db import models
from django.forms import ValidationError


def validate_username_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


def validate_unique_fruit_name(value):
    if Fruit.objects.filter(name=value).exists():
        raise ValidationError("This fruit name is already in use! Try a new one.")


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            MinLengthValidator(2),
            validate_username_only_letters,
            validate_unique_fruit_name,
        ],
    )
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nutrition = models.TextField(blank=False, null=False)
    owner = models.ForeignKey("user_profile.Profile", on_delete=models.CASCADE)
