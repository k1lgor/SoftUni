from django.forms import ValidationError


def validate_username_with_min_chars(value):
    if len(value) < 3:
        raise ValidationError("Username must be at least 3 chars long!")


def validate_username_alnum_or_underscore(value):
    is_valid = all(char.isalnum() or char == "_" for char in value)

    if not is_valid:
        raise ValidationError(
            "Username must contain only letters, digits, and underscores!"
        )

def validate_age_min_21(value):
    if value < 21:
        raise ValidationError("Age requirement: 21 years and above.")
