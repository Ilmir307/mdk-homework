"""Модуль чтения данных из файла (задание 1873)."""


def read_numbers(file_name):
    """Читает числа из файла (по одному в строке) и возвращает список.

    Пустые строки пропускаются. FileNotFoundError и ValueError
    обрабатываются вызывающей стороной.
    """
    numbers = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers
