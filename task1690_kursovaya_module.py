"""Программный модуль для курсовой работы (задание 1690).

Анализ результатов учебной сессии: программа читает оценки студентов
(с клавиатуры или из файла), рассчитывает статистику и выводит
результаты на экран и в файл отчёта.
"""

INPUT_FILE = "task1690-grades.txt"
REPORT_FILE = "task1690-report.txt"


def input_from_keyboard():
    """Ввод оценок с клавиатуры: числа через пробел."""
    raw = input("Введите оценки через пробел: ")
    return [float(x) for x in raw.split()]


def input_from_file(file_name):
    """Ввод оценок из файла: по одному числу в строке."""
    grades = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # пропускаем пустые строки
                grades.append(float(line))
    return grades


def process_data(grades):
    """Обработка данных: статистика по оценкам.

    На пустом списке выбрасывает ValueError.
    """
    if not grades:
        raise ValueError("список оценок пуст")
    return {
        "count": len(grades),
        "average": sum(grades) / len(grades),
        "minimum": min(grades),
        "maximum": max(grades),
        "sorted": sorted(grades, reverse=True),
    }


def format_report(stats):
    """Формирует текст отчёта из рассчитанной статистики."""
    lines = [
        "Отчёт по результатам сессии",
        "Оценок всего: " + str(stats["count"]),
        "Средний балл: " + str(round(stats["average"], 2)),
        "Минимальная оценка: " + str(stats["minimum"]),
        "Максимальная оценка: " + str(stats["maximum"]),
        "Оценки по убыванию: " + str(stats["sorted"]),
    ]
    return "\n".join(lines)


def save_report(file_name, text):
    """Сохраняет текст отчёта в файл."""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main():
    """Точка входа: выбор источника данных, обработка, вывод."""
    print("1. Ввод оценок с клавиатуры")
    print("2. Ввод оценок из файла")
    choice = input("Выберите источник данных: ")
    try:
        if choice == "1":
            grades = input_from_keyboard()
        elif choice == "2":
            grades = input_from_file(INPUT_FILE)
        else:
            print("Нет такого пункта меню")
            return
        stats = process_data(grades)
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return
    except ValueError as e:
        print("Ошибка в данных:", e)
        return
    report = format_report(stats)
    print(report)  # вывод на экран
    save_report(REPORT_FILE, report)  # и в файл
    print("Отчёт сохранён в файл:", REPORT_FILE)


if __name__ == "__main__":
    main()
