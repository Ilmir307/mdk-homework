"""Обработка данных из CSV с сохранением результатов в JSON (задание 1913).

Программа читает CSV-файл с оценками студентов (name;subject;score),
считает средний балл по каждому предмету (pandas) и общий средний
балл (numpy), формирует словарь с результатами и записывает его
в JSON-файл.
"""

import json

import numpy as np
import pandas as pd

INPUT_FILE = "task1913-scores.csv"
RESULT_FILE = "task1913-result.json"


def main():
    """Точка входа: CSV -> обработка pandas/numpy -> JSON."""
    try:
        # читаем CSV в DataFrame
        scores = pd.read_csv(INPUT_FILE, sep=";")
    except FileNotFoundError:
        print("Ошибка: файл '" + INPUT_FILE + "' не найден")
        return

    # обработка: средний балл по предметам (группировка pandas)
    by_subject = scores.groupby("subject")["score"].mean().round(2)
    subject_averages = by_subject.to_dict()

    # общая статистика (математические операции numpy)
    overall = {
        "overall_average": round(float(np.mean(scores["score"])), 2),
        "max_score": int(np.max(scores["score"])),
        "min_score": int(np.min(scores["score"])),
        "records_count": len(scores),
    }

    # формируем словарь с результатами и пишем в JSON
    result = {
        "subject_averages": subject_averages,
        "overall": overall,
    }
    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Средний балл по предметам:", subject_averages)
    print("Общая статистика:", overall)
    print("Результат сохранён в файл:", RESULT_FILE)


if __name__ == "__main__":
    main()
