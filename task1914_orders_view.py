"""Модуль ввода-вывода (консольный интерфейс) учёта заказов (задание 1914)."""


def print_menu():
    """Печатает меню команд."""
    print("1. Добавить заказ")
    print("2. Показать заказы")
    print("3. Общая сумма")
    print("0. Выход")


def ask_order():
    """Запрашивает у пользователя данные нового заказа.

    На нечисловом вводе количества или цены выбрасывает ValueError.
    """
    product = input("Товар: ")
    quantity = int(input("Количество: "))
    price = float(input("Цена: "))
    return product, quantity, price


def print_orders(orders):
    """Печатает список заказов."""
    if not orders:
        print("Заказов нет")
    for order in orders:
        print("#" + str(order["id"]), order["product"],
              "x" + str(order["quantity"]),
              "= " + str(order["total"]) + " руб.")
