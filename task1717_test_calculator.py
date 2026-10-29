"""Тестовые сценарии PyTest для модуля калькулятора (задание 1717)."""

import pytest

from task1717_calculator import add, divide, multiply, power, subtract


@pytest.fixture
def numbers():
    """Фикстура: пара чисел для арифметических тестов."""
    return (10, 5)


def test_add(numbers):
    """Сложение: 10 + 5 = 15."""
    a, b = numbers
    assert add(a, b) == 15


def test_add_negative():
    """Сложение с отрицательным числом: -5 + 3 = -2."""
    assert add(-5, 3) == -2


def test_subtract(numbers):
    """Вычитание: 10 - 5 = 5."""
    a, b = numbers
    assert subtract(a, b) == 5


def test_multiply(numbers):
    """Умножение: 10 * 5 = 50."""
    a, b = numbers
    assert multiply(a, b) == 50


def test_divide(numbers):
    """Деление: 10 / 5 = 2."""
    a, b = numbers
    assert divide(a, b) == 2


def test_divide_by_zero():
    """Деление на ноль выбрасывает ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    """Возведение в степень: 2 ** 10 = 1024."""
    assert power(2, 10) == 1024
