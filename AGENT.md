# AGENTS

## Project Overview

This document outlines the development standards, tools, and conventions used in the project.

### All actual versions of libraries and dependencies can be found in the `pyproject.toml` file.

## Testing Tools

### pytest

For testing and benchmarking, use pytest and libraries from its ecosystem.

- Write tests in `tests/` directory
- Tests should be organized in separate directories by functionality (e.g., unit, integration, etc.)
- Benchmark tests should be placed in a separate dedicated directory
- Use `pytest` for test execution
- Utilize `pytest-cov` for coverage analysis
- Consider `pytest-benchmark` for performance testing if needed

Run tests with coverage:

```bash
uv run pytest tests/ --cov=. --cov-report=term --cov-fail-under=80
```

This command is part of the Definition Of Done and ensures test coverage stays at or above 80%.

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
# Install all dependencies (runtime + dev + extras + tests)
uv sync --all-extras --group dev --group tests

# Install only runtime dependencies
uv sync

# Update dependencies and regenerate lock file
uv sync --refresh

# Add a new dependency
uv add package_name

# Add a dev dependency
uv add --group dev package_name

# Add a tests dependency
uv add --group tests package_name

# Remove a dependency
uv remove package_name

# Remove a dev dependency
uv remove --group dev package_name

# Remove a tests dependency
uv remove --group tests package_name

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
uv sync --all-extras

# Run full quality gate
uv tool install ruff ty pre_commit

# Install pre-commit hooks
uv run pre-commit install
```

### **Important**:

- After completing any task, you must run the full Definition Of Done checks to ensure code quality and consistency.
- Tests pass and coverage stays at or above `80%`
- Ruff passes without warnings
- Code must pass all `ruff` and `ty` checks
- All formatting changes must be applied with `ruff format`
- Docs/config changes stay aligned with the real file layout
- `uv.lock` is updated if dependencies change

#### Definition Of Done

```bash
uv run pre-commit run --all-files
uv run ruff format
uv run ruff check
uv run pytest tests/
```