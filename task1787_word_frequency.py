"""Частотный анализ текста: чтение файла, обработка, запись результата.

Задание 1787: интеграция программных модулей в Python.
Программа читает текст из файла, считает частоту слов
и сохраняет результат в другой файл. Каждая задача выделена
в отдельную функцию (логический модуль).
"""

INPUT_FILE = "task1787-text.txt"
RESULT_FILE = "task1787-result.txt"


# ---------- модуль чтения данных ----------

def read_text(file_name):
    """Читает весь текст из файла и возвращает его строкой."""
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()


# ---------- модуль обработки данных ----------

def count_words(text):
    """Считает частоту слов в тексте (регистр и знаки игнорируются)."""
    cleaned = "".join(ch.lower() if ch.isalnum() else " " for ch in text)
    counts = {}
    for word in cleaned.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def sort_by_frequency(counts):
    """Сортирует слова по убыванию частоты, при равенстве - по алфавиту."""
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


# ---------- модуль сохранения результата ----------

def save_result(file_name, sorted_words):
    """Записывает частотный список слов в файл."""
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Частотный анализ текста\n")
        for word, count in sorted_words:
            f.write(word + ": " + str(count) + "\n")


# ---------- основная часть ----------

def main():
    """Точка входа: чтение -> обработка -> сохранение."""
    try:
        text = read_text(INPUT_FILE)
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return
    counts = count_words(text)
    sorted_words = sort_by_frequency(counts)
    save_result(RESULT_FILE, sorted_words)
    print("Слов в тексте:", sum(counts.values()))
    print("Уникальных слов:", len(counts))
    print("Топ-3 частых слова:", sorted_words[:3])
    print("Результат сохранён в файл:", RESULT_FILE)


if __name__ == "__main__":
    main()
