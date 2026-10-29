"""Версия с проблемами: медленный поиск дублей и лишний расход памяти.

Задание 1740: анализ производительности и памяти.
"""


def find_duplicates_leaky(words):
    """Ищет повторяющиеся слова неэффективно.

    Проблемы:
    - вложенный цикл O(n^2) - на больших списках работает долго;
    - список copies хранит лишние копии всех строк (память);
    - список dead_result ниже вообще не используется.
    """
    copies = []
    for word in words:
        copies.append(word + word)  # ненужная удвоенная копия строки в памяти
    duplicates = []
    for i in range(len(copies)):
        for j in range(len(copies)):
            if i != j and copies[i] == copies[j]:
                if copies[i] not in duplicates:
                    duplicates.append(copies[i])
    return duplicates


def dead_code():
    """Мёртвая функция: никогда не вызывается (низкое покрытие)."""
    unused = "эта строка никогда не выполняется"
    return unused
