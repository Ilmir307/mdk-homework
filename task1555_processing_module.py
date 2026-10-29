"""Модуль обработки данных: сортировка и статистика по списку чисел.

Задание 1555: разработка и интеграция программных модулей.
"""


def sort_numbers(numbers, reverse=False):
    """Возвращает отсортированную копию списка чисел."""
    return sorted(numbers, reverse=reverse)


def get_statistics(numbers):
    """Считает статистику: количество, сумму, среднее, минимум, максимум.

    На пустом списке выбрасывает ValueError.
    """
    if not numbers:
        raise ValueError("список чисел пуст")
    return {
        "count": len(numbers),
        "total": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
    }
