"""Модуль доступа к API JSONPlaceholder: методы GET и POST (задание 1742)."""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    """GET-запрос: возвращает список публикаций из API."""
    response = requests.get(BASE_URL + "/posts", timeout=10)
    response.raise_for_status()  # кинет исключение при коде 4xx/5xx
    return response.json()


def create_post(title, body, user_id):
    """POST-запрос: создаёт публикацию и возвращает ответ сервера."""
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(BASE_URL + "/posts", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()
