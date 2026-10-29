"""Основной файл: интеграция модуля чтения и модуля сортировки.

Задание 1873: интеграция программных модулей в Python.
"""

import sys

from task1873_reader import read_numbers
from task1873_sorter import sort_numbers


def main():
    """Читает числа из файла (аргумент командной строки) и сортирует."""
    # имя файла берём из аргумента командной строки или используем умолчание
    file_name = sys.argv[1] if len(sys.argv) > 1 else "task1873-data.txt"
    try:
        numbers = read_numbers(file_name)
    except FileNotFoundError:
        print("Ошибка: файл '" + file_name + "' не найден")
        return
    except ValueError:
        print("Ошибка: в файле '" + file_name + "' есть нечисловые данные")
        return

    # передаём данные из модуля чтения в модуль сортировки
    print("Исходные данные:", numbers)
    print("По возрастанию:", sort_numbers(numbers))
    print("По убыванию:", sort_numbers(numbers, reverse=True))


if __name__ == "__main__":
    main()
