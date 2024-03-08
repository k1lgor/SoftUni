from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.models import Profile

from .validators import validate_year


class Car(models.Model):
    MIN_PRICE = 1.0
    MAX_TYPE_LENGTH = 10
    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1
    RALLY = "Rally"
    OPEN_WHEEL = "Open-wheel"
    KART = "Kart"
    DRAG = "Drag"
    OTHER = "Other"

    TYPE_CHOICES = (
        (RALLY, RALLY),
        (OPEN_WHEEL, OPEN_WHEEL),
        (KART, KART),
        (DRAG, DRAG),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
    )
    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH),
        ],
    )
    year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=[
            validate_year,
        ],
    )
    image_url = models.URLField(
        blank=False,
        null=False,
        unique=True,
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(MIN_PRICE),
        ],
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
