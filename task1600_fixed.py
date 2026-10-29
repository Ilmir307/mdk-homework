"""Учёт товаров: исправленный вариант кода после анализа Pylint.

Задание 1600: анализ качества кода статическим анализатором Pylint.
"""


class Product:
    """Товар с названием и ценой."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        """Возвращает цену товара."""
        return self.price

    def apply_discount(self, percent):
        """Применяет скидку в процентах и возвращает новую цену."""
        self.price = self.price * (100 - percent) / 100
        return self.price


def calc_total(items):
    """Считает суммарную стоимость списка товаров."""
    total = 0
    for item in items:
        total = total + item.get_price()
    return total


if __name__ == "__main__":
    my_list = [Product("Хлеб", 50), Product("Молоко", 80)]
    print("Итого: " + str(calc_total(my_list)))
