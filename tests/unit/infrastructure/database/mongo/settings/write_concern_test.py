from src.infrastructure.database.mongo.settings.constants import (
    WriteConcernDefaults,
)
from src.infrastructure.database.mongo.settings.write_concern import (
    WriteConcernSettings,
)


def test_write_concern_settings_default_values() -> None:
    """Test that WriteConcernSettings initializes with default values from WriteConcernDefaults."""
    # Arrange
    expected_w = WriteConcernDefaults.W
    expected_journal = WriteConcernDefaults.JOURNAL
    expected_fsync = WriteConcernDefaults.FSYNC

    # Act
    settings = WriteConcernSettings()

    # Assert
    assert expected_w == settings.W
    assert expected_journal == settings.JOURNAL
    assert expected_fsync == settings.FSYNC


def test_write_concern_settings_custom_values() -> None:
    """Test that WriteConcernSettings properly sets custom values for all fields."""
    # Arrange
    custom_w = "majority"
    custom_journal = True
    custom_fsync = True

    # Act
    settings = WriteConcernSettings(
        W=custom_w, JOURNAL=custom_journal, FSYNC=custom_fsync
    )

    # Assert
    assert custom_w == settings.W
    assert settings.JOURNAL is custom_journal
    assert settings.FSYNC is custom_fsync


def test_write_concern_settings_client_kwargs_returns_dict() -> None:
    """Test that client_kwargs property returns a dictionary."""
    # Arrange
    settings = WriteConcernSettings()

    # Act
    result = settings.client_kwargs

    # Assert
    assert isinstance(result, dict)


def test_write_concern_settings_client_kwargs_with_defaults() -> None:
    """Test that client_kwargs returns correct values with default settings."""
    # Arrange
    expected_journal = WriteConcernDefaults.JOURNAL
    expected_fsync = WriteConcernDefaults.FSYNC
    settings = WriteConcernSettings()

    # Act
    result = settings.client_kwargs

    # Assert
    assert "w" not in result
    assert result["journal"] == expected_journal
    assert result["fsync"] == expected_fsync


def test_write_concern_settings_client_kwargs_with_w_value() -> None:
    """Test that client_kwargs includes 'w' key when W has a value."""
    # Arrange
    w_value = 2
    expected_journal = WriteConcernDefaults.JOURNAL
    expected_fsync = WriteConcernDefaults.FSYNC
    settings = WriteConcernSettings(W=w_value)

    # Act
    result = settings.client_kwargs

    # Assert
    assert result["w"] == w_value
    assert result["journal"] == expected_journal
    assert result["fsync"] == expected_fsync


def test_write_concern_settings_client_kwargs_with_w_majority() -> None:
    """Test that client_kwargs includes 'w' key with 'majority' value when W is 'majority'."""
    # Arrange
    w_value = "majority"
    expected_journal = WriteConcernDefaults.JOURNAL
    expected_fsync = WriteConcernDefaults.FSYNC
    settings = WriteConcernSettings(W=w_value)

    # Act
    result = settings.client_kwargs

    # Assert
    assert result["w"] == w_value
    assert result["journal"] == expected_journal
    assert result["fsync"] == expected_fsync


def test_write_concern_settings_client_kwargs_with_w_none() -> None:
    """Test that client_kwargs does not include 'w' key when W is None."""
    # Arrange
    w_value = None
    expected_journal = WriteConcernDefaults.JOURNAL
    expected_fsync = WriteConcernDefaults.FSYNC
    settings = WriteConcernSettings(W=w_value)

    # Act
    result = settings.client_kwargs

    # Assert
    assert "w" not in result
    assert result["journal"] == expected_journal
    assert result["fsync"] == expected_fsync


def test_write_concern_settings_client_kwargs_with_journal_false() -> None:
    """Test that client_kwargs includes journal=False when JOURNAL is False."""
    # Arrange
    journal_value = False
    expected_fsync = WriteConcernDefaults.FSYNC
    settings = WriteConcernSettings(JOURNAL=journal_value)

    # Act
    result = settings.client_kwargs

    # Assert
    assert result["journal"] is journal_value
    assert result["fsync"] == expected_fsync


def test_write_concern_settings_client_kwargs_with_fsync_false() -> None:
    """Test that client_kwargs includes fsync=False when FSYNC is False."""
    # Arrange
    fsync_value = False
    expected_journal = WriteConcernDefaults.JOURNAL
    settings = WriteConcernSettings(FSYNC=fsync_value)

    # Act
    result = settings.client_kwargs

    # Assert
    assert result["journal"] == expected_journal
    assert result["fsync"] is fsync_value


def test_write_concern_settings_client_kwargs_with_all_custom_values() -> None:
    """Test that client_kwargs returns correct values with all custom settings."""
    # Arrange
    w_value = "majority"
    journal_value = True
    fsync_value = True
    settings = WriteConcernSettings(
        W=w_value, JOURNAL=journal_value, FSYNC=fsync_value
    )

    # Act
    result = settings.client_kwargs

    # Assert
    assert result["w"] == w_value
    assert result["journal"] is journal_value
    assert result["fsync"] is fsync_value
