from app.exceptions import ValidationError


def validate_number(value):
    """Validate and convert input to float."""

    # LBYL (Look Before You Leap)
    if value is None:
        raise ValidationError("Value cannot be None.")

    # EAFP (Easier to Ask Forgiveness than Permission)
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValidationError(f"Invalid number: {value}")