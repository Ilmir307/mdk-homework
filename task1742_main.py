"""Основной файл: GET/POST к API и обмен данными между модулями.

Задание 1742: работа с API и обмен данными между модулями.
"""

import requests

from task1742_api_module import create_post, get_posts
from task1742_processing_module import count_posts_by_user, make_summary


def main():
    """Выполняет GET и POST к API, передаёт данные модулю обработки."""
    try:
        # GET: получаем публикации из API
        posts = get_posts()
    except requests.RequestException as e:
        print("Ошибка при обращении к API:", e)
        return

    print("GET-запрос: получено публикаций:", len(posts))
    print()

    # передаём данные модулю обработки: статистика по пользователям
    counts = count_posts_by_user(posts)
    print("Публикаций по пользователям:")
    for user_id, count in sorted(counts.items()):
        print("  userId", user_id, "->", count)
    print()

    # передаём данные модулю обработки: первые 3 заголовка
    print("Первые публикации:")
    for position, post in enumerate(posts[:3], start=1):
        print(make_summary(post, position))
    print()

    # POST: создаём новую публикацию через API
    new_post = create_post("Учебный пост", "Проверка POST из задания 1742", 1)
    print("POST-запрос: сервер вернул id =", new_post.get("id"))
    print("Сервер сохранил заголовок:", new_post.get("title"))


if __name__ == "__main__":
    main()
