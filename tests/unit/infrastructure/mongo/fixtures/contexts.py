from unittest.mock import Mock

import pytest
from bson.codec_options import DatetimeConversion

from src.infrastructure.mongo.contexts import (
    ClientContex,
    InitBeanieContex,
)


@pytest.fixture
def default_client_context():
    """Создает контекст клиента со значениями по умолчанию"""
    return ClientContex()


@pytest.fixture
def custom_client_context():
    """Создает контекст клиента с кастомными значениями"""
    return ClientContex(
        tz_aware=True,
        datetime_conversion=DatetimeConversion.DATETIME_CLAMP,
        document_class=dict,
        type_registry=Mock(),
        server_selector=Mock(),
        event_listeners=(Mock(), Mock()),
    )


@pytest.fixture
def client_context_with_driver():
    """Создает контекст клиента с Mock драйвера"""
    mock_driver = Mock()
    mock_driver.name = "test-driver"
    mock_driver.version = "1.0.0"

    return ClientContex(driver=mock_driver, tz_aware=True)


@pytest.fixture
def client_context_with_encryption():
    """Создает контекст клиента с опциями шифрования"""
    mock_encryption = Mock()
    mock_encryption.kms_providers = {"aws": {"access_key_id": "test"}}

    return ClientContex(
        auto_encryption_opts=mock_encryption,
        datetime_conversion=DatetimeConversion.DATETIME_AUTO,
    )


@pytest.fixture
def client_context_with_server_api():
    """Создает контекст клиента с Server API"""
    mock_server_api = Mock()
    mock_server_api.version = "1"

    return ClientContex(
        server_api=mock_server_api,
        server_selector=Mock(),
        event_listeners=(Mock(), Mock(), Mock()),
    )


@pytest.fixture(
    params=[
        DatetimeConversion.DATETIME,
        DatetimeConversion.DATETIME_AUTO,
        DatetimeConversion.DATETIME_CLAMP,
        DatetimeConversion.DATETIME_MS,
    ]
)
def client_context_with_datetime_conversion(request):
    """Параметризованная фикстура для всех типов конвертации даты/времени"""
    return ClientContex(
        datetime_conversion=request.param,
        tz_aware=request.param == DatetimeConversion.DATETIME,
    )


@pytest.fixture
def client_context_all_params():
    """Создает контекст клиента со всеми возможными параметрами"""
    mock_driver = Mock()
    mock_encryption = Mock()
    mock_server_api = Mock()
    mock_type_registry = Mock()
    mock_server_selector = Mock()

    return ClientContex(
        tz_aware=True,
        datetime_conversion=DatetimeConversion.DATETIME_MS,
        document_class=dict,
        type_registry=mock_type_registry,
        server_selector=mock_server_selector,
        driver=mock_driver,
        event_listeners=(Mock(), Mock()),
        auto_encryption_opts=mock_encryption,
        server_api=mock_server_api,
    )


# === Фикстуры для InitBeanieContex ===


@pytest.fixture
def default_beanie_context():
    """Создает Beanie контекст со значениями по умолчанию"""
    return InitBeanieContex()


@pytest.fixture
def custom_beanie_context():
    """Создает Beanie контекст с кастомными значениями"""
    return InitBeanieContex(
        allow_index_dropping=True, recreate_views=True, skip_indexes=False
    )


@pytest.fixture
def beanie_context_all_true():
    """Создает Beanie контекст со всеми флагами True"""
    return InitBeanieContex(
        allow_index_dropping=True, recreate_views=True, skip_indexes=True
    )


@pytest.fixture
def beanie_context_all_false():
    """Создает Beanie контекст со всеми флагами False"""
    return InitBeanieContex(
        allow_index_dropping=False, recreate_views=False, skip_indexes=False
    )


@pytest.fixture(
    params=[
        (True, True, True),
        (True, True, False),
        (True, False, True),
        (True, False, False),
        (False, True, True),
        (False, True, False),
        (False, False, True),
        (False, False, False),
    ]
)
def beanie_context_combinations(request):
    """Параметризованная фикстура для всех комбинаций булевых значений"""
    allow_drop, recreate, skip = request.param
    return InitBeanieContex(
        allow_index_dropping=allow_drop,
        recreate_views=recreate,
        skip_indexes=skip,
    ), request.param


@pytest.fixture
def beanie_context_with_index_dropping():
    """Beanie контекст с разрешенным удалением индексов"""
    return InitBeanieContex(
        allow_index_dropping=True, recreate_views=False, skip_indexes=False
    )


@pytest.fixture
def beanie_context_with_views_recreation():
    """Beanie контекст с пересозданием представлений"""
    return InitBeanieContex(
        allow_index_dropping=False, recreate_views=True, skip_indexes=False
    )


@pytest.fixture
def beanie_context_skip_indexes():
    """Beanie контекст с пропуском создания индексов"""
    return InitBeanieContex(
        allow_index_dropping=False, recreate_views=False, skip_indexes=True
    )
