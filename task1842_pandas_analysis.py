"""Анализ продаж из CSV с помощью pandas и numpy (задание 1842).

Программа читает CSV-файл с продажами (date;product;quantity;price),
группирует продажи по товарам, считает выручку и средний чек
и сохраняет итоги в новый CSV-файл.
"""

import numpy as np
import pandas as pd

INPUT_FILE = "task1842-sales.csv"
RESULT_FILE = "task1842-result.csv"


def main():
    """Точка входа: CSV -> обработка pandas/numpy -> CSV."""
    try:
        # читаем CSV в DataFrame (модуль pandas)
        sales = pd.read_csv(INPUT_FILE, sep=";")
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return

    # добавляем столбец выручки по строке
    sales["revenue"] = sales["quantity"] * sales["price"]

    # группируем по товару: штуки и выручка (агрегации pandas)
    report = sales.groupby("product").agg(
        total_quantity=("quantity", "sum"),
        total_revenue=("revenue", "sum"),
    ).reset_index()

    # средний чек по товару (модуль numpy)
    report["average_check"] = np.round(
        report["total_revenue"] / report["total_quantity"], 2)

    # сортируем по выручке и сохраняем результат
    report = report.sort_values("total_revenue", ascending=False)
    report.to_csv(RESULT_FILE, sep=";", index=False)

    print(report.to_string(index=False))
    print()
    print("Всего выручка:", sales["revenue"].sum())
    print("Средняя цена продажи (numpy.mean):",
          round(float(np.mean(sales["price"])), 2))
    print("Результат сохранён в файл:", RESULT_FILE)


if __name__ == "__main__":
    main()
