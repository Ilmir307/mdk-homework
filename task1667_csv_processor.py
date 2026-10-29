"""Обработка данных CSV: чтение, фильтрация, сортировка, запись.

Задание 1667: интеграция программных модулей в Python.
Программа читает CSV-файл со списком товаров (name;price;quantity),
отбрасывает товары с нулевым остатком, сортирует остальные по цене
и записывает результат в новый CSV-файл.
"""

import csv

INPUT_FILE = "task1667-input.csv"
OUTPUT_FILE = "task1667-output.csv"
FIELDS = ["name", "price", "quantity"]


def read_csv(file_name):
    """Читает данные из CSV-файла и возвращает список строк-словарей.

    Если заголовок не совпадает с ожидаемым, выбрасывает ValueError.
    """
    with open(file_name, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        if reader.fieldnames != FIELDS:
            raise ValueError("некорректный заголовок CSV-файла")
        return list(reader)


def process_data(data):
    """Обрабатывает данные: фильтрация по остатку и сортировка по цене.

    Текстовые поля переводятся в числа; товары с нулевым остатком
    отбрасываются. Если в поле не число, выбрасывается ValueError.
    """
    processed = []
    for row in data:
        row["price"] = float(row["price"])
        row["quantity"] = int(row["quantity"])
        if row["quantity"] > 0:  # товар без остатка в выгрузку не идёт
            processed.append(row)
    return sorted(processed, key=lambda row: row["price"])


def write_csv(file_name, data):
    """Записывает список строк-словарей в CSV-файл с заголовком."""
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter=";")
        writer.writeheader()
        writer.writerows(data)


def main():
    """Точка входа: связывает чтение, обработку и запись."""
    try:
        data = read_csv(INPUT_FILE)
        processed = process_data(data)
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return
    except ValueError as e:
        print("Ошибка в данных файла:", e)
        return

    write_csv(OUTPUT_FILE, processed)
    print("Прочитано строк:", len(data))
    print("После фильтрации:", len(processed))
    for row in processed:
        print(row["name"], "-", row["price"], "руб.,", row["quantity"], "шт.")
    print("Результат записан в файл:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
