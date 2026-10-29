"""Интеграционный модуль: stdin -> обработка -> stdout (задание 1604).

Читает из стандартного ввода строки вида 'Имя Возраст'
и выводит в стандартный вывод 'Имя: {имя}, Возраст: {возраст}'.
"""

import sys


def parse_person(line):
    """Разбирает строку 'Имя Возраст' в пару (имя, возраст).

    На неверном формате выбрасывает ValueError.
    """
    parts = line.split()
    if len(parts) != 2:
        raise ValueError("ожидается формат: Имя Возраст")
    name = parts[0]
    age = int(parts[1])  # ValueError, если возраст не число
    return name, age


def main():
    """Читает строки из stdin и печатает результат в stdout."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # пустые строки пропускаем
        try:
            name, age = parse_person(line)
        except ValueError as e:
            print("Ошибка:", e)
            continue
        print("Имя: " + name + ", Возраст: " + str(age))


if __name__ == "__main__":
    main()
