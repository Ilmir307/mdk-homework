"""Модуль обработки данных: сортировка (задание 1873)."""


def sort_numbers(numbers, reverse=False):
    """Возвращает отсортированную копию списка чисел.

    Исходный список не изменяется: sorted() создаёт новый список.
    """
    return sorted(numbers, reverse=reverse)
