"""Оптимизированная версия поиска дублей (задание 1740).

Исправления после анализа:
- множества вместо вложенного цикла: сложность O(n) вместо O(n^2);
- лишние копии строк убраны - память не расходуется зря;
- мёртвый код удалён.
"""


def find_duplicates(words):
    """Возвращает отсортированный список повторяющихся слов."""
    seen = set()
    duplicates = set()
    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)
    return sorted(duplicates)
