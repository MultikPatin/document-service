from dataclasses import FrozenInstanceError

import pytest


class TestInitBeanieContex:
    """Тесты для InitBeanieContex с использованием фикстур"""

    def test_default_values(self, default_beanie_context):
        """Проверка значений по умолчанию"""
        assert default_beanie_context.allow_index_dropping is False
        assert default_beanie_context.recreate_views is False
        assert default_beanie_context.skip_indexes is False

    def test_custom_values(self, custom_beanie_context):
        """Проверка кастомных значений"""
        assert custom_beanie_context.allow_index_dropping is True
        assert custom_beanie_context.recreate_views is True
        assert custom_beanie_context.skip_indexes is False

    def test_all_true(self, beanie_context_all_true):
        """Проверка всех флагов True"""
        assert beanie_context_all_true.allow_index_dropping is True
        assert beanie_context_all_true.recreate_views is True
        assert beanie_context_all_true.skip_indexes is True

    def test_all_false(self, beanie_context_all_false):
        """Проверка всех флагов False"""
        assert beanie_context_all_false.allow_index_dropping is False
        assert beanie_context_all_false.recreate_views is False
        assert beanie_context_all_false.skip_indexes is False

    def test_all_combinations(self, beanie_context_combinations):
        """Параметризованный тест для всех комбинаций булевых значений"""
        context, (allow_drop, recreate, skip) = beanie_context_combinations
        assert context.allow_index_dropping == allow_drop
        assert context.recreate_views == recreate
        assert context.skip_indexes == skip

    def test_with_index_dropping(self, beanie_context_with_index_dropping):
        """Проверка контекста с разрешенным удалением индексов"""
        assert beanie_context_with_index_dropping.allow_index_dropping is True
        assert beanie_context_with_index_dropping.recreate_views is False

    def test_with_views_recreation(self, beanie_context_with_views_recreation):
        """Проверка контекста с пересозданием представлений"""
        assert beanie_context_with_views_recreation.recreate_views is True
        assert beanie_context_with_views_recreation.skip_indexes is False

    def test_skip_indexes(self, beanie_context_skip_indexes):
        """Проверка контекста с пропуском индексов"""
        assert beanie_context_skip_indexes.skip_indexes is True
        assert beanie_context_skip_indexes.allow_index_dropping is False

    def test_immutability(self, default_beanie_context):
        """Проверка неизменяемости объекта"""
        with pytest.raises(FrozenInstanceError):
            default_beanie_context.allow_index_dropping = True
