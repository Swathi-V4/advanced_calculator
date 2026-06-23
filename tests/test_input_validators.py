import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError


@pytest.mark.parametrize(
    "value,expected",
    [
        ("10", 10.0),
        ("3.14", 3.14),
        (5, 5.0),
    ],
)
def test_validate_number(value, expected):
    assert validate_number(value) == expected


def test_validate_none():
    with pytest.raises(ValidationError):
        validate_number(None)


def test_validate_invalid():
    with pytest.raises(ValidationError):
        validate_number("abc")