"""Модуль ввода данных: чтение чисел из текстового файла.

Задание 1555: разработка и интеграция программных модулей.
"""


def read_numbers(file_name):
    """Читает числа из файла (по одному в строке) и возвращает список.

    Пустые строки пропускаются. FileNotFoundError (нет файла) и
    ValueError (не число в строке) обрабатываются вызывающей стороной.
    """
    numbers = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # пропускаем пустые строки
                numbers.append(float(line))
    return numbers
