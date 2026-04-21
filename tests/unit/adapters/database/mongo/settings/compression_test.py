import pytest
from pydantic import ValidationError

from libs.mongo.constants.settings import (
    CompressionDefaults as D,
)
from libs.mongo.settings.compression import (
    CompressionSettings,
)


def test_compression_settings_default(
    default_compression_settings, default_compression_client_kwargs
):
    """Test default values for CompressionSettings."""
    s = default_compression_settings
    assert s.COMPRESSORS == D.COMPRESSORS
    assert s.ZLIB_COMPRESSION_LEVEL == D.ZLIB_COMPRESSION_LEVEL
    assert s.client_kwargs == default_compression_client_kwargs


@pytest.mark.parametrize(
    "compressor",
    ["snappy", "zlib", "zstd", None],
    ids=["snappy", "zlib", "zstd", "none"],
)
def test_compression_settings_valid_compressor(compressor):
    """Test valid compressor values."""
    settings = CompressionSettings(COMPRESSORS=compressor)
    assert compressor == settings.COMPRESSORS

    expected_kwargs = {}
    if compressor:
        expected_kwargs["compressors"] = compressor
    assert settings.client_kwargs == expected_kwargs


@pytest.mark.parametrize(
    "level",
    [*list(range(10)), None],
    ids=[
        "level-0",
        "level-1",
        "level-2",
        "level-3",
        "level-4",
        "level-5",
        "level-6",
        "level-7",
        "level-8",
        "level-9",
        "none",
    ],
)
def test_compression_settings_valid_zlib_level(level):
    """Test valid zlib compression level values."""
    settings = CompressionSettings(ZLIB_COMPRESSION_LEVEL=level)
    assert level == settings.ZLIB_COMPRESSION_LEVEL

    expected_kwargs = {}
    if isinstance(level, int) and level > 0:
        expected_kwargs["zlibCompressionLevel"] = level
    assert settings.client_kwargs == expected_kwargs


@pytest.mark.parametrize(
    ("compressor", "level", "expected_kwargs"),
    [
        ("zlib", 6, {"compressors": "zlib", "zlibCompressionLevel": 6}),
        ("zstd", 3, {"compressors": "zstd", "zlibCompressionLevel": 3}),
        ("snappy", 0, {"compressors": "snappy"}),
        ("zlib", None, {"compressors": "zlib"}),
        (None, 5, {"zlibCompressionLevel": 5}),
    ],
)
def test_compression_settings_valid_combinations(
    compressor, level, expected_kwargs
):
    """Test valid combinations of compressor and zlib level."""
    settings = CompressionSettings(
        COMPRESSORS=compressor, ZLIB_COMPRESSION_LEVEL=level
    )
    assert compressor == settings.COMPRESSORS
    assert level == settings.ZLIB_COMPRESSION_LEVEL
    assert settings.client_kwargs == expected_kwargs


def test_compression_settings_client_kwargs_only_compressor():
    """Test client_kwargs includes only compressors when only COMPRESSORS is set."""
    settings = CompressionSettings(COMPRESSORS="snappy")
    assert settings.client_kwargs == {"compressors": "snappy"}
    assert "zlibCompressionLevel" not in settings.client_kwargs


def test_compression_settings_client_kwargs_only_zlib_level():
    """Test client_kwargs includes only zlibCompressionLevel when only ZLIB_COMPRESSION_LEVEL is set."""
    settings = CompressionSettings(ZLIB_COMPRESSION_LEVEL=9)
    assert settings.client_kwargs == {"zlibCompressionLevel": 9}
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


@pytest.mark.parametrize(
    "value",
    ["invalid", "gzip", "lz4", "123"],
)
def test_compression_settings_invalid_compressor(value):
    """Test invalid compressor values raise validation error."""
    with pytest.raises(ValidationError):
        CompressionSettings(COMPRESSORS=value)


def test_compression_settings_invalid_zlib_level_out_of_range_below():
    """Test invalid zlib compression level values below range raise validation error."""
    for value in [-1, -5]:
        with pytest.raises(ValidationError):
            CompressionSettings(ZLIB_COMPRESSION_LEVEL=value)


def test_compression_settings_invalid_zlib_level_out_of_range_above():
    """Test invalid zlib compression level values above range raise validation error."""
    for value in [10, 15]:
        with pytest.raises(ValidationError):
            CompressionSettings(ZLIB_COMPRESSION_LEVEL=value)


def test_compression_settings_invalid_zlib_level_non_integer():
    """Test invalid non-integer zlib compression level values raise validation error."""
    for value in ["invalid", 3.5]:
        with pytest.raises(ValidationError):
            CompressionSettings(ZLIB_COMPRESSION_LEVEL=value)


def test_compression_settings_invalid_zlib_level_string_integer():
    """Test string that could be integer but is invalid due to range raises validation error."""
    with pytest.raises(ValidationError):
        CompressionSettings(ZLIB_COMPRESSION_LEVEL="10")


@pytest.mark.parametrize(
    ("compressor", "level"),
    [
        ("invalid", 6),
        ("lz4", 3),
        ("gzip", 0),
    ],
)
def test_compression_settings_invalid_compressor_combinations(
    compressor, level
):
    """Test combinations with invalid compressor values raise validation error."""
    with pytest.raises(ValidationError):
        CompressionSettings(
            COMPRESSORS=compressor, ZLIB_COMPRESSION_LEVEL=level
        )


def test_compression_settings_invalid_zlib_level_combinations():
    """Test combinations with invalid zlib level values raise validation error."""
    with pytest.raises(ValidationError):
        CompressionSettings(COMPRESSORS="zlib", ZLIB_COMPRESSION_LEVEL=-1)

    with pytest.raises(ValidationError):
        CompressionSettings(COMPRESSORS="zlib", ZLIB_COMPRESSION_LEVEL=10)
