"""Калькулятор с обработкой исключений (задание 1715).

Выполняет арифметические операции и корректно обрабатывает ошибки:
нечисловой ввод, неизвестная операция, деление на ноль.
"""

HISTORY_FILE = "task1715-history.txt"


def calculate(a, operator, b):
    """Выполняет операцию над двумя числами и возвращает результат.

    На неизвестной операции выбрасывает ValueError,
    при делении на ноль - ZeroDivisionError.
    """
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b  # при b == 0 возникнет ZeroDivisionError
    raise ValueError("неизвестная операция '" + operator + "'")


def read_number(prompt):
    """Запрашивает число; на нечисловом вводе выбрасывает ValueError."""
    return float(input(prompt))


def save_history(text):
    """Дописывает строку вычисления в файл истории."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def main():
    """Точка входа: ввод, вычисление, обработка исключений."""
    try:
        a = read_number("Первое число: ")
        operator = input("Операция (+, -, *, /): ")
        b = read_number("Второе число: ")
        result = calculate(a, operator, b)
    except ValueError as e:
        # сюда попадают и нечисловой ввод, и неизвестная операция
        print("Ошибка: некорректное значение.", e)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль. Второе число не должно быть 0")
    else:
        # выполняется, только если исключений не было
        print("Результат:", result)
        save_history(str(a) + " " + operator + " " + str(b)
                     + " = " + str(result))
        print("Запись добавлена в историю:", HISTORY_FILE)
    finally:
        # выполняется всегда - и при ошибке тоже
        print("Завершение работы программы")


if __name__ == "__main__":
    main()
