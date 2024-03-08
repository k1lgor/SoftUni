from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_plant_name(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")


class Plant(models.Model):
    TYPE_CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )
    plant_type = models.CharField(max_length=14, choices=TYPE_CHOICES)
    plant_name = models.CharField(
        max_length=20, validators=[validate_plant_name, MinLengthValidator(2)]
    )
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
