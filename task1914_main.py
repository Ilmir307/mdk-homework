"""Основной файл: интеграция модулей учёта заказов (задание 1914).

Приложение состоит из трёх модулей: хранение данных (OrderBook),
консольный ввод-вывод и основной модуль, связывающий их через меню.
"""

from task1914_orders_store import OrderBook
from task1914_orders_view import ask_order, print_menu, print_orders

DATA_FILE = "task1914-orders.json"


def main():
    """Цикл приложения: меню -> модули хранения и отображения."""
    book = OrderBook()
    book.load(DATA_FILE)  # подхватываем заказы прошлых запусков
    while True:
        print_menu()
        try:
            choice = input("Выберите пункт: ")
        except EOFError:
            break  # конец потока ввода - выходим
        if choice == "1":
            try:
                product, quantity, price = ask_order()
            except ValueError:
                print("Ошибка: количество и цена должны быть числами")
                continue
            order_id = book.add_order(product, quantity, price)
            book.save(DATA_FILE)
            print("Заказ добавлен, номер:", order_id)
        elif choice == "2":
            print_orders(book.get_all())
        elif choice == "3":
            print("Общая сумма заказов:", book.get_total_sum(), "руб.")
        elif choice == "0":
            print("Выход")
            break
        else:
            print("Нет такого пункта")
        print()


if __name__ == "__main__":
    main()
