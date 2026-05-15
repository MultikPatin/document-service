from dataclasses import FrozenInstanceError

import pytest
from bson.codec_options import DatetimeConversion


class TestClientContex:
    """Тесты для ClientContex с использованием фикстур"""

    def test_default_values(self, default_client_context):
        """Проверка значений по умолчанию"""
        assert default_client_context.tz_aware is False
        assert (
            default_client_context.datetime_conversion
            == DatetimeConversion.DATETIME
        )
        assert default_client_context.document_class is None
        assert default_client_context.driver is None
        assert default_client_context.event_listeners == ()

    def test_custom_values(self, custom_client_context):
        """Проверка кастомных значений"""
        excepted_len = 2

        assert custom_client_context.tz_aware is True
        assert (
            custom_client_context.datetime_conversion
            == DatetimeConversion.DATETIME_CLAMP
        )
        assert custom_client_context.document_class is dict
        assert len(custom_client_context.event_listeners) == excepted_len

    def test_with_driver(self, client_context_with_driver):
        """Проверка контекста с драйвером"""
        assert client_context_with_driver.driver is not None
        assert client_context_with_driver.driver.name == "test-driver"
        assert client_context_with_driver.tz_aware is True

    def test_with_encryption(self, client_context_with_encryption):
        """Проверка контекста с шифрованием"""
        assert client_context_with_encryption.auto_encryption_opts is not None
        assert (
            client_context_with_encryption.datetime_conversion
            == DatetimeConversion.DATETIME_AUTO
        )

    def test_with_server_api(self, client_context_with_server_api):
        """Проверка контекста с Server API"""
        excepted_len = 3

        assert client_context_with_server_api.server_api is not None
        assert client_context_with_server_api.server_selector is not None
        assert (
            len(client_context_with_server_api.event_listeners) == excepted_len
        )

    def test_datetime_conversion_parametrized(
        self, client_context_with_datetime_conversion
    ):
        """Параметризованный тест для всех типов конвертации даты/времени"""
        assert isinstance(
            client_context_with_datetime_conversion.datetime_conversion,
            DatetimeConversion,
        )

    def test_all_params(self, client_context_all_params):
        """Проверка контекста со всеми параметрами"""
        excepted_len = 2

        assert client_context_all_params.tz_aware is True
        assert (
            client_context_all_params.datetime_conversion
            == DatetimeConversion.DATETIME_MS
        )
        assert client_context_all_params.document_class is dict
        assert client_context_all_params.type_registry is not None
        assert client_context_all_params.server_selector is not None
        assert client_context_all_params.driver is not None
        assert len(client_context_all_params.event_listeners) == excepted_len
        assert client_context_all_params.auto_encryption_opts is not None
        assert client_context_all_params.server_api is not None

    def test_immutability(self, default_client_context):
        """Проверка неизменяемости объекта"""
        with pytest.raises(FrozenInstanceError):
            default_client_context.tz_aware = True
