"""Основной файл: обмен данными между модулями через API (задание 1713).

Модуль API получает данные из внешнего сервиса, передаёт их модулю
обработки, а результат выводится пользователю.
"""

from task1713_api_module import get_users
from task1713_processing_module import count_domains, extract_contacts


def main():
    """Получает пользователей из API и передаёт их модулю обработки."""
    try:
        users = get_users()
    except OSError as e:
        print("Ошибка при обращении к API:", e)
        return
    print("Получено пользователей:", len(users))
    print()
    print("Контакты:")
    for name, email in extract_contacts(users):
        print(" ", name, "-", email)
    print()
    print("Домены e-mail:")
    for domain, count in count_domains(users).items():
        print(" ", domain + ":", count)


if __name__ == "__main__":
    main()
