import pytest
from pydantic import ValidationError

from libs.mongo.constants.settings import (
    ErrorHandlingDefaults as D,
)
from libs.mongo.settings.erro_handling import (
    ErrorHandlingSettings,
)


def test_error_handling_settings_default(
    default_error_handling_settings, default_error_handling_client_kwargs
) -> None:
    """Test default values for ErrorHandlingSettings."""
    s = default_error_handling_settings

    assert s.UNICODE_DECODE == D.UNICODE_DECODE
    assert s.client_kwargs == default_error_handling_client_kwargs


@pytest.mark.parametrize(
    "unicode_decode_value",
    ["strict", "ignore", "replace", "backslashreplace", "surrogateescape"],
    ids=["strict", "ignore", "replace", "backslashreplace", "surrogateescape"],
)
def test_valid_unicode_decode_values(unicode_decode_value: str) -> None:
    """Test that valid unicode_decode values are accepted."""
    settings = ErrorHandlingSettings(UNICODE_DECODE=unicode_decode_value)
    assert unicode_decode_value == settings.UNICODE_DECODE


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("strict", {"unicode_decode_error_handler": "strict"}),
        ("ignore", {"unicode_decode_error_handler": "ignore"}),
    ],
    ids=["strict", "ignore"],
)
def test_client_kwargs_returns_correct_dict(value, expected) -> None:
    """Test that client_kwargs property returns correct dictionary."""
    settings = ErrorHandlingSettings(UNICODE_DECODE=value)
    assert settings.client_kwargs == expected


def test_client_kwargs_returns_new_dict_each_time() -> None:
    """Test that client_kwargs returns a new dictionary instance each time."""
    settings = ErrorHandlingSettings(UNICODE_DECODE="strict")
    dict1 = settings.client_kwargs
    dict2 = settings.client_kwargs
    assert dict1 is not dict2
    assert dict1 == dict2


@pytest.mark.parametrize(
    "value",
    ["invalid", "", "random_value", "STRICT", "IGNORE"],
    ids=["invalid", "empty", "random", "uppercase-strict", "uppercase-ignore"],
)
def test_invalid_unicode_decode_values(value) -> None:
    """Test that invalid unicode_decode values raise ValidationError."""
    with pytest.raises(ValidationError):
        ErrorHandlingSettings(UNICODE_DECODE=value)
