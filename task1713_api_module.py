"""Модуль доступа к API: получение данных из JSONPlaceholder.

Задание 1713: работа с API и обмен данными между модулями.
"""

import json
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(path):
    """Выполняет GET-запрос к API и возвращает данные объектом.

    При сетевых ошибках выбрасывает OSError (обрабатывается в main).
    """
    with urllib.request.urlopen(BASE_URL + path, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def get_users():
    """Возвращает список пользователей из API."""
    return get_json("/users")
