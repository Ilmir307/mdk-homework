"""Программный модуль «Калькулятор» для тестирования (задание 1717)."""


def add(a, b):
    """Сложение."""
    return a + b


def subtract(a, b):
    """Вычитание."""
    return a - b


def multiply(a, b):
    """Умножение."""
    return a * b


def divide(a, b):
    """Деление; на нулевом делителе выбрасывает ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("деление на ноль")
    return a / b


def power(base, exponent):
    """Возведение в степень."""
    return base ** exponent
