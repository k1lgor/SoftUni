from django.db import models

from profiles.validators import (
    validate_age_min_21,
    validate_username_alnum_or_underscore,
    validate_username_with_min_chars,
)


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MAX_PASSWORD_LENGTH = 20
    MAX_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        blank=False,
        null=False,
        validators=[
            validate_username_with_min_chars,
            validate_username_alnum_or_underscore,
        ],
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    age = models.PositiveIntegerField(
        help_text="Age requirement: 21 years and above.",
        blank=False,
        null=False,
        validators=[
            validate_age_min_21,
        ],
    )
    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
