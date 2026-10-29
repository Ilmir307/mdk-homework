"""Сравнение роста памяти: утечка против исправленной версии (задание 1603)."""

import tracemalloc

import task1603_fixed
import task1603_leaky

ROUNDS = 20
VALUES_PER_ROUND = 1000


def main():
    """Гоняет обе версии и замеряет текущее потребление памяти."""
    tracemalloc.start()
    for _ in range(ROUNDS):
        task1603_leaky.process_data(list(range(VALUES_PER_ROUND)))
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("С утечкой (глобальный кэш):", round(current / 1024 / 1024, 1), "МБ")

    tracemalloc.start()
    cache = []
    for _ in range(ROUNDS):
        task1603_fixed.process_data(list(range(VALUES_PER_ROUND)), cache)
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("После исправления (лимит кэша):", round(current / 1024 / 1024, 3),
          "МБ")
    print("Записей в кэше после исправления:", len(cache),
          "(лимит:", task1603_fixed.CACHE_LIMIT, ")")


if __name__ == "__main__":
    main()
