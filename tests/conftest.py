# import pytest

pytest_plugins = [
    "tests.unit.infrastructure.mongo.fixtures.contexts",
]

# Можно добавить глобальные хуки и конфигурации


def pytest_configure(config):
    """Конфигурация pytest при запуске"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )


# @pytest.fixture(scope="session", autouse=True)
# def session_setup():
#     """Глобальная настройка для всей тестовой сессии"""
#     print("\nSetting up test session...")
#     yield
#     print("\nTearing down test session...")
#
#
# @pytest.fixture(scope="module")
# def module_setup():
#     """Настройка для каждого модуля тестов"""
#     print("\nSetting up module...")
#     yield
#     print("\nTearing down module...")
