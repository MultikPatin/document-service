# AGENTS

## Project Overview

This document outlines the development standards, tools, and conventions used in the project.

### All actual versions of libraries and dependencies can be found in the `pyproject.toml` file.

### Project Layout

```
project/              # Корень проекта
├── deployment/       # Файлы сборки и деплоя
│   └── ...
├── documentation/    # Документация к проекту
│   └── ...
├── src/              # Исходный код
│   └── ...
├── tests/            # Корень тестов
│   ├── conftest.py   # Глобальные настройки и pytest_plugins
│   ├── fixtures/     # Все фикстуры по модулям
│   │   ├──...
│   └── unit/         # Тесты юнитов
│   │   ├──...
│   └── integration/  # Тесты интеграции
│   │   ├──...
│   └───...
├── pyproject.toml    # Файл конфигурации для проекта
├── ruff.toml         # Конфигурацяи ruff
├── ty.toml           # Конфгурациия ty
└── pytest.ini        # Конфигурация pytest
```

## Development Tools

### Package Manager: uv

Project uses `uv` as the primary package manager for dependency management and execution.

#### Key Features

- Fast dependency resolution and installation
- Poetry-compatible with `pyproject.toml`
- Virtual environment management
- Lock file generation (`uv.lock`) for deterministic builds

#### Common Commands

```bash
# Install all dependencies (runtime + dev + extras)
uv sync --all-extras --group dev

# Install only runtime dependencies
uv sync

# Update dependencies and regenerate lock file
uv sync --refresh

# Add a new dependency
uv add package_name

# Add a dev dependency
uv add --group dev package_name

# Remove a dependency
uv remove package_name

# Remove a dev dependency
uv remove --group dev package_name

# Create virtual environment
uv venv

# Run commands in project environment
uv run <command>
```

### Code Quality: Ruff and ty

#### **Important**: They are installed as a uv tool

```bash
# Show available
uv tool list

# Install package
uv tool install package_name

# UnInstall packge
uv tool uninstall package_name
```

#### Ruff

Ruff is the primary formatter and linter, combining multiple Python tools into a single fast solution.

**Configuration**
Located in `ruff.toml`, includes rules for:

- Code style (PEP 8)
- Code quality checks
- Import sorting
- Line length limits
- Project-specific rules

**Commands**

```bash
# Check code for issues
uv run ruff check .

# Show potential fixes
uv run ruff check . --diff

# Apply automatic fixes
uv run ruff check . --fix

# Format all Python files
uv run ruff format .

# Check formatting without changes
uv run ruff format --check .

# Show formatting changes
uv run ruff format --diff .
```

#### ty

`ty` is used for building type-safe command-line interfaces with automatic help generation.

**Configuration**
Located in `ty.toml`, includes:

- Command structure
- Argument definitions
- Option types
- Help text
- Version information

**Commands**

```bash
# Check code for issues
uv run ty check .
```

### Pre-commit Hooks

Pre-commit hooks are used to ensure code quality before commits.

**Commands**

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run pre-commit manually
uv run pre-commit run --all-files
```

## Development Conventions

### Universal Conventions

- **Formatter/Linter:** Ruff is the project standard. Keep `ruff check` and `ruff format` green.
- **CLI Tool:** Project uses `ty` for command-line interface development.
- **Commit style:** Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `ci:`.
- **Python compatibility:** Code must remain compatible with Python `3.10` through `3.14`.
- **Async-first:** Endpoint handlers and upstream GigaChat interactions are async.
- **Imports:** stdlib → third-party → local (`src.*`), using absolute imports.
- **Docstrings:** Google style, imperative mood, concise.

### Security & Secrets

- **Never commit secrets** such as `.env`, credentials, API keys, or local cert/key material.
- `MODE=PROD` requires an API key and disables `/docs`, `/redoc`, `/openapi.json`, and `/logs*`.
- Prefer `.env` or environment variables for secrets; do not pass secrets via CLI flags.

## Development Workflow

### Setup Commands

```bash
# Install runtime
uv sync --all-extras --group dev
# Run full quality gate
uv tool install ruff ty pre_commit
# Install pre-commit hooks
uv run pre-commit install
```

**Note**: Use `--group` arguments only if the corresponding group is defined in `pyproject.toml`.

### **Important**:

- After completing any task, you must run the full Definition Of Done checks to ensure code quality and consistency.
- Tests pass and coverage stays at or above `80%`
- Ruff passes without warnings
- Code must pass all `ruff` and `ty` checks
- All formatting changes must be applied with `ruff format`
- Docs/config changes stay aligned with the real file layout
- `uv.lock` is updated if dependencies change

#### Definition Of Task Done

Run to ensure everything works fine and task is completed. All check must succeed

```bash
uv run ruff format .
uv run ruff check . --fix
uv run pytest tests/
uv run pre-commit run --all-files
```

## Testing

### pytest

For testing, use pytest and libraries from its ecosystem.

- Use `pytest` for test execution
- Use `pytest-asyncio` for async support
- Utilize `pytest-cov` for coverage analysis

Run tests:

```bash
uv run pytest tests/
```

### Test Implementation Guidelines

- Use `@pytest.mark.parametrize` decorator whenever possible to test multiple input combinations in a single test
  function
- Always extract reusable test data and setup logic into fixtures
- When creating a new fixture file, add its path to `pytest_plugins` list in `tests/conftest.py` to make fixtures
  available across the test suite
- Error tests should be placed in separate functions and located at the end of the test file, after all positive tests
- Do not verify the exact text of error messages in tests, only verify the type and structure of exceptions

### Test Structure and Naming Conventions

- **Directory Structure**: Tests are located in the `tests/` directory, with subdirectories by type (e.g., `unit/`,
  `integration/`). The path within `tests/` mirrors `src/`. For example, `src/core/settings.py` →
  `tests/unit/core/settings/model_config_test.py`. The `unit/` directory is already present in the project structure.
- **File Naming**: Test files should follow the pattern `*_test.py` (e.g., `model_config_test.py`). This aligns with
  common Python practices and ensures pytest discovers them automatically.
- **Function Naming**: Test functions must be prefixed with `test_` (e.g., `test_validate_settings()`).
- **Class Naming**: Test classes should be named with the prefix `Test` followed by the name of the class being tested (
  e.g., `TestSettingsModel`).
- **PEP Standards**: Adhere to PEP 8 for code style and PEP 257 for docstring conventions. Tests should be readable,
  concise, and include meaningful docstrings when necessary.
