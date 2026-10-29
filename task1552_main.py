# Основной файл: интеграция модуля данных и модуля обработки
# Задание 1552: интеграция программных модулей в Python

from task1552_data_module import read_data_from_file
from task1552_processing_module import sort_data

DATA_FILE = "task1552-data.txt"


def main():
    # читаем данные из файла через модуль данных
    try:
        data = read_data_from_file(DATA_FILE)
    except FileNotFoundError:
        print("Ошибка: файл '" + DATA_FILE + "' не найден")
        return
    except ValueError:
        print("Ошибка: в файле '" + DATA_FILE + "' есть нечисловые данные")
        return

    print("Исходные данные:", data)

    # передаём данные в модуль обработки и выводим результат
    sorted_data = sort_data(data)
    print("Отсортированные данные:", sorted_data)


if __name__ == "__main__":
    main()
