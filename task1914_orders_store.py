"""Модуль хранения данных о заказах (задание 1914)."""

import json


class OrderBook:
    """Хранит заказы и умеет сохранять/загружать их в JSON-файл."""

    def __init__(self):
        self.orders = []

    def add_order(self, product, quantity, price):
        """Добавляет заказ и возвращает его номер."""
        order = {
            "id": len(self.orders) + 1,
            "product": product,
            "quantity": quantity,
            "price": price,
            "total": quantity * price,
        }
        self.orders.append(order)
        return order["id"]

    def get_all(self):
        """Возвращает список всех заказов."""
        return self.orders

    def get_total_sum(self):
        """Возвращает сумму всех заказов."""
        return sum(order["total"] for order in self.orders)

    def save(self, file_name):
        """Сохраняет заказы в JSON-файл."""
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(self.orders, f, ensure_ascii=False, indent=2)

    def load(self, file_name):
        """Загружает заказы из JSON-файла, если он существует."""
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                self.orders = json.load(f)
        except FileNotFoundError:
            pass  # файла ещё нет - начинаем с пустого списка
