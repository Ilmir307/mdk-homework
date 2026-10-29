"""Событийно-управляемая программа: консольный список покупок.

Задание 1225: событийно-управляемое программирование.
Программа работает в цикле событий: каждая введённая команда —
событие, которое обрабатывает свой обработчик из таблицы HANDLERS.
"""


def on_add(state, arg):
    """Обработчик события 'add': добавляет товар в список."""
    if not arg:
        print("Ошибка: укажите товар (например: add хлеб)")
        return
    state["items"].append(arg)
    print("Добавлено:", arg)


def on_list(state, arg):
    """Обработчик события 'list': показывает список покупок."""
    if not state["items"]:
        print("Список пуст")
    for i, item in enumerate(state["items"], start=1):
        print(str(i) + ".", item)


def on_remove(state, arg):
    """Обработчик события 'remove': удаляет товар по номеру."""
    try:
        index = int(arg) - 1
        removed = state["items"].pop(index)
        print("Удалено:", removed)
    except (ValueError, IndexError):
        print("Ошибка: нет товара с таким номером")


def on_exit(state, arg):
    """Обработчик события 'exit': останавливает цикл событий."""
    state["running"] = False
    print("Программа завершена")


# таблица событие -> его обработчик
HANDLERS = {
    "add": on_add,
    "list": on_list,
    "remove": on_remove,
    "exit": on_exit,
}


def main():
    """Цикл событий: читаем команду и вызываем её обработчик."""
    state = {"items": [], "running": True}
    print("Команды: add <товар>, list, remove <номер>, exit")
    while state["running"]:
        try:
            raw = input("> ")
        except EOFError:
            break  # конец потока ввода - завершаем цикл событий
        parts = raw.split(maxsplit=1)
        event = parts[0].lower() if parts and parts[0] else ""
        arg = parts[1] if len(parts) > 1 else ""
        handler = HANDLERS.get(event)
        if handler is None:
            print("Неизвестное событие:", event)
        else:
            handler(state, arg)  # реагируем на событие


if __name__ == "__main__":
    main()
