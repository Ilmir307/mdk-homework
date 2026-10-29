"""Исправленная версия после отладки (задание 1605)."""


def find_max(numbers):
    """Возвращает максимум списка чисел.

    На пустом списке выбрасывает ValueError.
    """
    if not numbers:
        raise ValueError("список пуст")
    max_num = numbers[0]  # стартуем с первого элемента, а не с нуля
    for number in numbers[1:]:
        if number > max_num:
            max_num = number
    return max_num


def average(numbers):
    """Возвращает среднее арифметическое списка чисел.

    На пустом списке выбрасывает ValueError.
    """
    if not numbers:
        raise ValueError("среднее пустого списка не определено")
    return sum(numbers) / len(numbers)


def main():
    """Проверяет функции на наборах, ломавших исходную версию."""
    data = [5, 3, 8, 1]
    print("Максимум:", find_max(data))
    print("Среднее:", average(data))
    print("Максимум отрицательных:", find_max([-5, -3]))
    print("Максимум [9, 1, 2]:", find_max([9, 1, 2]))
    for func, arg in ((find_max, []), (average, [])):
        try:
            func(arg)
        except ValueError as e:
            print("Пустой список -> понятная ошибка:", e)


if __name__ == "__main__":
    main()
