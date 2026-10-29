"""Исправленная версия: ограниченный кэш и корректный файл (задание 1603)."""

CACHE_LIMIT = 100


def process_data(values, cache):
    """Обрабатывает данные; кэш ограничен CACHE_LIMIT последними записями.

    Файл открывается через with и гарантированно закрывается.
    """
    for value in values:
        cache.append(str(value) * 1000)
        if len(cache) > CACHE_LIMIT:
            del cache[:-CACHE_LIMIT]  # держим только последние записи
    with open("task1603-log.txt", "a", encoding="utf-8") as f:
        f.write("обработано " + str(len(values)) + "\n")
    return len(values)
