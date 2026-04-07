import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.compression import (
    CompressionSettings,
)


def test_compression_settings_valid_compressor():
    """Test valid compressor values."""
    # Test each valid compressor
    for compressor in ["snappy", "zlib", "zstd"]:
        settings = CompressionSettings(COMPRESSORS=compressor)
        assert compressor == settings.COMPRESSORS
        assert settings.client_kwargs == {"compressors": compressor}

    # Test None compressor
    settings = CompressionSettings(COMPRESSORS=None)
    assert settings.COMPRESSORS is None
    assert settings.client_kwargs == {}


def test_compression_settings_valid_zlib_level():
    """Test valid zlib compression level values."""
    # Test valid levels 0-9
    for level in range(10):
        settings = CompressionSettings(ZLIB_COMPRESSION_LEVEL=level)
        assert level == settings.ZLIB_COMPRESSION_LEVEL
        expected_kwargs = {} if level == 0 else {"zlibCompressionLevel": level}
        assert settings.client_kwargs == expected_kwargs

    # Test None level
    settings = CompressionSettings(ZLIB_COMPRESSION_LEVEL=None)
    assert settings.ZLIB_COMPRESSION_LEVEL is None
    assert settings.client_kwargs == {}


def test_compression_settings_invalid_compressor():
    """Test invalid compressor values raise validation error."""
    invalid_values = ["invalid", "gzip", "lz4", "123"]

    for value in invalid_values:
        with pytest.raises(ValidationError):
            CompressionSettings(COMPRESSORS=value)


def test_compression_settings_invalid_zlib_level():
    """Test invalid zlib compression level values raise validation error."""
    # Test invalid integer values below range
    for value in [-1, -5]:
        with pytest.raises(ValidationError):
            CompressionSettings(ZLIB_COMPRESSION_LEVEL=value)

    # Test invalid integer values above range
    for value in [10, 15]:
        with pytest.raises(ValidationError):
            CompressionSettings(ZLIB_COMPRESSION_LEVEL=value)

    # Test invalid non-integer values
    for value in ["invalid", 3.5]:
        with pytest.raises(ValidationError):
            CompressionSettings(ZLIB_COMPRESSION_LEVEL=value)

    # Test string that could be integer but is invalid due to range
    with pytest.raises(ValidationError):
        CompressionSettings(ZLIB_COMPRESSION_LEVEL="10")


def test_compression_settings_both_fields():
    """Test both fields set simultaneously."""
    # Test valid combination
    expected_level = 6
    settings = CompressionSettings(
        COMPRESSORS="zlib", ZLIB_COMPRESSION_LEVEL=expected_level
    )
    assert settings.COMPRESSORS == "zlib"
    assert expected_level == settings.ZLIB_COMPRESSION_LEVEL
    assert settings.client_kwargs == {
        "compressors": "zlib",
        "zlibCompressionLevel": expected_level,
    }

    # Test combination with invalid compressor
    with pytest.raises(ValidationError):
        CompressionSettings(COMPRESSORS="invalid", ZLIB_COMPRESSION_LEVEL=6)

    # Test combination with invalid level
    with pytest.raises(ValidationError):
        CompressionSettings(COMPRESSORS="zlib", ZLIB_COMPRESSION_LEVEL=-1)


def test_compression_settings_client_kwargs_empty():
    """Test client_kwargs returns empty dict when no values set."""
    settings = CompressionSettings()
    assert settings.COMPRESSORS is None
    assert settings.ZLIB_COMPRESSION_LEVEL is None
    assert settings.client_kwargs == {}


def test_compression_settings_client_kwargs_only_compressor():
    """Test client_kwargs includes only compressors when only COMPRESSORS is set."""
    settings = CompressionSettings(COMPRESSORS="snappy")
    assert settings.client_kwargs == {"compressors": "snappy"}

    # Verify ZLIB_COMPRESSION_LEVEL is not in kwargs when not set
    assert "zlibCompressionLevel" not in settings.client_kwargs


def test_compression_settings_client_kwargs_only_zlib_level():
    """Test client_kwargs includes only zlibCompressionLevel when only ZLIB_COMPRESSION_LEVEL is set."""
    settings = CompressionSettings(ZLIB_COMPRESSION_LEVEL=9)
    assert settings.client_kwargs == {"zlibCompressionLevel": 9}

    # Verify compressors is not in kwargs when not set
    assert "compressors" not in settings.client_kwargs


def test_compression_settings_client_kwargs_both_present():
    """Test client_kwargs includes both keys when both fields have values."""
    settings = CompressionSettings(COMPRESSORS="zstd", ZLIB_COMPRESSION_LEVEL=3)
    assert settings.client_kwargs == {
        "compressors": "zstd",
        "zlibCompressionLevel": 3,
    }


def test_compression_settings_client_kwargs_none_values():
    """Test client_kwargs excludes keys when values are None."""
    # Even if explicitly set to None
    settings = CompressionSettings(
        COMPRESSORS=None, ZLIB_COMPRESSION_LEVEL=None
    )
    assert settings.client_kwargs == {}

    # Mixed case with one None
    settings = CompressionSettings(
        COMPRESSORS="snappy", ZLIB_COMPRESSION_LEVEL=None
    )
    assert settings.client_kwargs == {"compressors": "snappy"}

    settings = CompressionSettings(COMPRESSORS=None, ZLIB_COMPRESSION_LEVEL=5)
    assert settings.client_kwargs == {"zlibCompressionLevel": 5}
