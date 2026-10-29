# Модуль для работы с данными: чтение чисел из текстового файла
# Задание 1552: интеграция программных модулей в Python


def read_data_from_file(file_name):
    """Читает числа из файла (по одному в строке) и возвращает список.

    Пустые строки пропускаются. Если файл не найден, выбрасывает
    FileNotFoundError, а если в строке не число - ValueError;
    обе ошибки обрабатываются в основном файле main.
    """
    data = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # пропускаем пустые строки
                data.append(float(line))
    return data
