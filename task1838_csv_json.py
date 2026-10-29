"""Чтение CSV, обработка и вывод в консоль и JSON (задание 1838).

Программа читает список сотрудников из CSV-файла (name;department;salary),
выбирает сотрудников отдела разработки, сортирует их по убыванию
зарплаты, выводит результат в консоль и сохраняет в файлы
console_output.txt и json_output.json.

Модули (логические секции): чтение CSV, обработка, вывод.
"""

import csv
import json

INPUT_FILE = "task1838-input.csv"
CONSOLE_FILE = "console_output.txt"
JSON_FILE = "json_output.json"
FIELDS = ["name", "department", "salary"]


# ---------- модуль чтения данных из CSV ----------

def read_csv(file_name):
    """Читает CSV-файл и возвращает список строк-словарей."""
    with open(file_name, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        if reader.fieldnames != FIELDS:
            raise ValueError("некорректный заголовок CSV-файла")
        return list(reader)


# ---------- модуль обработки данных ----------

def process_data(data):
    """Фильтрует разработчиков и сортирует их по убыванию зарплаты."""
    developers = []
    for row in data:
        row["salary"] = float(row["salary"])  # текст -> число
        if row["department"] == "Разработка":
            developers.append(row)
    return sorted(developers, key=lambda row: -row["salary"])


# ---------- модуль вывода: консоль и JSON ----------

def print_and_save_console(lines):
    """Печатает строки в консоль и дублирует их в console_output.txt."""
    for line in lines:
        print(line)
    with open(CONSOLE_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def save_json(file_name, data):
    """Сохраняет список словарей в JSON-файл с кириллицей."""
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    """Точка входа: CSV -> обработка -> консоль и JSON."""
    try:
        data = read_csv(INPUT_FILE)
        developers = process_data(data)
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return
    except ValueError as e:
        print("Ошибка в данных файла:", e)
        return

    lines = ["Сотрудники отдела разработки (по убыванию зарплаты):"]
    for row in developers:
        lines.append(row["name"] + " - " + str(row["salary"]) + " руб.")
    print_and_save_console(lines)

    save_json(JSON_FILE, developers)
    print("Результаты сохранены:", CONSOLE_FILE, "и", JSON_FILE)


if __name__ == "__main__":
    main()
