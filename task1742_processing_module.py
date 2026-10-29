"""Модуль обработки данных, полученных из API (задание 1742)."""


def count_posts_by_user(posts):
    """Считает, сколько публикаций приходится на каждого пользователя."""
    counts = {}
    for post in posts:
        user_id = post["userId"]
        counts[user_id] = counts.get(user_id, 0) + 1
    return counts


def make_summary(post, position):
    """Формирует строку краткого описания публикации для вывода."""
    return str(position) + ". " + post["title"]
