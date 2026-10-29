"""Модуль обработки данных, полученных из API (задание 1713)."""


def extract_contacts(users):
    """Извлекает из списка пользователей пары (имя, e-mail)."""
    return [(user["name"], user["email"]) for user in users]


def count_domains(users):
    """Считает, сколько пользователей приходится на каждый домен e-mail."""
    domains = {}
    for user in users:
        domain = user["email"].split("@")[-1]
        domains[domain] = domains.get(domain, 0) + 1
    return domains
