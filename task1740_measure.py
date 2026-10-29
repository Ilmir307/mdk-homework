"""Замер времени и памяти для двух версий поиска дублей (задание 1740)."""

import time
import tracemalloc

from task1740_leaky import find_duplicates_leaky
from task1740_optimized import find_duplicates

WORDS_COUNT = 5000


def make_words(count):
    """Генерирует список слов: каждое десятое слово - повтор."""
    words = []
    for i in range(count):
        if i % 10 == 0 and words:
            words.append(words[-1])  # дублируем предыдущее слово
        else:
            words.append("word" + str(i))
    return words


def measure(func, data):
    """Замеряет время выполнения и пиковую память функции."""
    tracemalloc.start()
    start = time.perf_counter()
    result = func(data)
    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, elapsed, peak


def main():
    """Сравнивает исходную и оптимизированную версии."""
    words = make_words(WORDS_COUNT)
    print("Слов в списке:", len(words))
    for func in (find_duplicates_leaky, find_duplicates):
        result, elapsed, peak = measure(func, words)
        print(func.__name__ + ":")
        print("  дублей найдено:", len(result))
        print("  время: " + str(round(elapsed, 3)) + " с")
        print("  пиковая память: " + str(round(peak / 1024, 1)) + " КБ")


if __name__ == "__main__":
    main()
