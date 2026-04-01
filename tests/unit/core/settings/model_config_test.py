from src.core.settings.constants import _MODEL_CONFIG_DEFAULTS
from src.core.settings.model_config import model_config


def test_with_no_args() -> None:
    """Test model_config with no arguments uses all defaults."""
    config = model_config()

    assert config["env_file"] == _MODEL_CONFIG_DEFAULTS["env_file"]
    assert (
        config["env_file_encoding"]
        == _MODEL_CONFIG_DEFAULTS["env_file_encoding"]
    )
    assert (
        config["env_nested_delimiter"]
        == _MODEL_CONFIG_DEFAULTS["env_nested_delimiter"]
    )
    assert config["extra"] == _MODEL_CONFIG_DEFAULTS["extra"]
    assert config["frozen"] == _MODEL_CONFIG_DEFAULTS["frozen"]


def test_with_partial_args() -> None:
    """Test model_config with partial arguments uses provided values and defaults for others."""
    config = model_config(
        env_file=".env.prod",
        extra="allow",
    )

    assert config["env_file"] == ".env.prod"
    assert (
        config["env_file_encoding"]
        == _MODEL_CONFIG_DEFAULTS["env_file_encoding"]
    )
    assert (
        config["env_nested_delimiter"]
        == _MODEL_CONFIG_DEFAULTS["env_nested_delimiter"]
    )
    assert config["extra"] == "allow"
    assert config["frozen"] == _MODEL_CONFIG_DEFAULTS["frozen"]


def test_with_all_args() -> None:
    """Test model_config with all arguments overrides all defaults."""
    config = model_config(
        env_file=".env.custom",
        env_file_encoding="latin-1",
        env_nested_delimiter="::",
        extra="forbid",
        frozen=False,
    )

    assert config["env_file"] == ".env.custom"
    assert config["env_file_encoding"] == "latin-1"
    assert config["env_nested_delimiter"] == "::"
    assert config["extra"] == "forbid"
    assert config["frozen"] is False


def test_preserves_unknown_args() -> None:
    """Test that model_config preserves any additional arguments passed to it."""
    config = model_config(
        cli_prog_name="custom_value",
        cli_flag_prefix_char="cli_flag_prefix_char",
    )

    assert "cli_prog_name" in config
    assert config["cli_prog_name"] == "custom_value"
    assert "cli_flag_prefix_char" in config
    assert config["cli_flag_prefix_char"] == "cli_flag_prefix_char"

    # Verify defaults are still applied for known parameters
    assert config["env_file"] == _MODEL_CONFIG_DEFAULTS["env_file"]
    assert config["frozen"] == _MODEL_CONFIG_DEFAULTS["frozen"]


def test_merges_with_defaults() -> None:
    """Test that model_config properly merges provided args with defaults."""
    provided_args = {
        "env_file": ".env.test",
        "extra": "allow",
    }
    config = model_config(**provided_args)

    # Check provided values
    assert config["env_file"] == ".env.test"
    assert config["extra"] == "allow"

    # Check default values for non-provided keys
    assert (
        config["env_file_encoding"]
        == _MODEL_CONFIG_DEFAULTS["env_file_encoding"]
    )
    assert (
        config["env_nested_delimiter"]
        == _MODEL_CONFIG_DEFAULTS["env_nested_delimiter"]
    )
    assert config["frozen"] == _MODEL_CONFIG_DEFAULTS["frozen"]
