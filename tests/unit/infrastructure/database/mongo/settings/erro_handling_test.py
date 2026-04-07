import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.erro_handling import (
    ErrorHandlingSettings,
)


class TestErrorHandlingSettings:
    """Test suite for ErrorHandlingSettings Pydantic model."""

    @pytest.mark.parametrize(
        "unicode_decode_value",
        ["strict", "ignore", "replace", "backslashreplace", "surrogateescape"],
    )
    def test_valid_unicode_decode_values(
        self, unicode_decode_value: str
    ) -> None:
        """Test that valid unicode_decode values are accepted."""
        settings = ErrorHandlingSettings(UNICODE_DECODE=unicode_decode_value)
        assert unicode_decode_value == settings.UNICODE_DECODE

    @pytest.mark.parametrize(
        "unicode_decode_value",
        ["invalid", "", "random_value", "STRICT", "IGNORE"],
    )
    def test_invalid_unicode_decode_values(
        self, unicode_decode_value: str
    ) -> None:
        """Test that invalid unicode_decode values raise ValidationError."""
        with pytest.raises(ValidationError):
            ErrorHandlingSettings(UNICODE_DECODE=unicode_decode_value)

    def test_client_kwargs_returns_correct_dict(self) -> None:
        """Test that client_kwargs property returns correct dictionary."""
        settings = ErrorHandlingSettings(UNICODE_DECODE="strict")
        expected = {"unicode_decode_error_handler": "strict"}
        assert settings.client_kwargs == expected

        settings = ErrorHandlingSettings(UNICODE_DECODE="ignore")
        expected = {"unicode_decode_error_handler": "ignore"}
        assert settings.client_kwargs == expected

    def test_client_kwargs_returns_new_dict_each_time(self) -> None:
        """Test that client_kwargs returns a new dictionary instance each time."""
        settings = ErrorHandlingSettings(UNICODE_DECODE="strict")
        dict1 = settings.client_kwargs
        dict2 = settings.client_kwargs
        assert dict1 is not dict2
        assert dict1 == dict2
