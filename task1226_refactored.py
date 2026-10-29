"""Расчёт суммы заказа со скидкой (после рефакторинга, задание 1226)."""

DISCOUNT_RATE = 0.1  # скидка постоянным покупателям, 10 %


def calculate_total(prices, with_discount=False):
    """Возвращает сумму заказа; при with_discount применяет скидку."""
    total = sum(prices)
    if with_discount:
        total = total * (1 - DISCOUNT_RATE)
    return total


def main():
    """Проверяет расчёт на демонстрационном наборе цен."""
    prices = [100, 200, 50]
    print("Без скидки:", calculate_total(prices))
    print("Со скидкой:", calculate_total(prices, with_discount=True))


if __name__ == "__main__":
    main()
