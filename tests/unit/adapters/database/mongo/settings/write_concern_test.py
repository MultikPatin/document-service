import pytest
from libs.mongo.constants.settings import (
    WriteConcernDefaults as D,
)
from libs.mongo.settings import (
    WriteConcernSettings,
)


def test_write_concern_settings_default(
    default_write_concern_settings, default_write_concern_client_kwargs
) -> None:
    """Test default values for WriteConcernSettings."""
    s = default_write_concern_settings

    assert s.W == D.W
    assert s.JOURNAL == D.JOURNAL
    assert s.FSYNC == D.FSYNC
    assert s.client_kwargs == default_write_concern_client_kwargs


@pytest.mark.parametrize(
    ("w_value", "journal_value", "fsync_value"),
    [
        (
            D.W,
            D.JOURNAL,
            D.FSYNC,
        ),
        ("majority", True, True),
        (2, False, True),
        (None, True, False),
    ],
)
def test_write_concern_settings_initialization(
    w_value, journal_value, fsync_value
) -> None:
    """Test that WriteConcernSettings properly initializes with various combinations of values."""
    # Act
    settings = WriteConcernSettings(
        W=w_value, JOURNAL=journal_value, FSYNC=fsync_value
    )

    # Assert
    assert w_value == settings.W
    assert settings.JOURNAL is journal_value
    assert settings.FSYNC is fsync_value


def test_write_concern_settings_client_kwargs_returns_dict(
    default_write_concern_settings,
) -> None:
    """Test that client_kwargs property returns a dictionary."""
    # Act
    result = default_write_concern_settings.client_kwargs

    # Assert
    assert isinstance(result, dict)


@pytest.mark.parametrize(
    ("journal_value", "fsync_value", "expected_journal", "expected_fsync"),
    [
        (
            D.JOURNAL,
            D.FSYNC,
            D.JOURNAL,
            D.FSYNC,
        ),
        (True, False, True, False),
        (False, True, False, True),
    ],
)
def test_write_concern_settings_client_kwargs_without_w(
    journal_value, fsync_value, expected_journal, expected_fsync
) -> None:
    """Test that client_kwargs returns correct values when W is not set."""
    # Arrange
    settings = WriteConcernSettings(JOURNAL=journal_value, FSYNC=fsync_value)

    # Act
    result = settings.client_kwargs

    # Assert
    assert "w" not in result
    assert result["journal"] == expected_journal
    assert result["fsync"] == expected_fsync


@pytest.mark.parametrize(
    ("w_value", "journal_value", "fsync_value"),
    [
        (2, D.JOURNAL, D.FSYNC),
        ("majority", True, False),
        (1, False, True),
    ],
)
def test_write_concern_settings_client_kwargs_with_w_value(
    w_value, journal_value, fsync_value
) -> None:
    """Test that client_kwargs includes 'w' key when W has a value."""
    # Arrange
    settings = WriteConcernSettings(
        W=w_value, JOURNAL=journal_value, FSYNC=fsync_value
    )

    # Act
    result = settings.client_kwargs

    # Assert
    assert result["w"] == w_value
    assert result["journal"] == journal_value
    assert result["fsync"] == fsync_value
