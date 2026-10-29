"""Основной файл: интеграция модулей ввода, обработки и вывода.

Задание 1555: разработка и интеграция программных модулей.
Модули связаны последовательно: вывод одного — вход другого.
"""

from task1555_input_module import read_numbers
from task1555_output_module import print_statistics, save_result
from task1555_processing_module import get_statistics, sort_numbers

INPUT_FILE = "task1555-data.txt"
RESULT_FILE = "task1555-result.txt"


def main():
    """Точка входа: связывает модули в единое приложение."""
    # модуль ввода: читаем числа из файла
    try:
        numbers = read_numbers(INPUT_FILE)
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return
    except ValueError:
        print("Ошибка: в файле '" + INPUT_FILE + "' есть нечисловые данные")
        return
    print("Прочитано чисел:", len(numbers))

    # модуль обработки: сортировка и статистика
    sorted_numbers = sort_numbers(numbers)
    stats = get_statistics(numbers)

    # модуль вывода: печать и сохранение в файл
    print("Отсортированные данные:", sorted_numbers)
    print_statistics(stats)
    save_result(RESULT_FILE, sorted_numbers, stats)
    print("Результат сохранён в файл:", RESULT_FILE)


if __name__ == "__main__":
    main()
