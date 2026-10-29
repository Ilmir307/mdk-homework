"""Модуль вывода данных: печать и сохранение результатов в файл.

Задание 1555: разработка и интеграция программных модулей.
"""


def print_statistics(stats):
    """Печатает статистику по списку чисел."""
    print("Количество чисел:", stats["count"])
    print("Сумма:", stats["total"])
    print("Среднее:", stats["average"])
    print("Минимум:", stats["minimum"])
    print("Максимум:", stats["maximum"])


def save_result(file_name, numbers, stats):
    """Сохраняет отсортированный список и статистику в файл."""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Отсортированные данные: " + str(numbers) + "\n")
        for key, value in stats.items():
            f.write(key + ": " + str(value) + "\n")
