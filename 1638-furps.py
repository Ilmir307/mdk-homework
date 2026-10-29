# Классификация требований по компонентам модели FURPS+
# Задание 1638: анализ требований к мобильному приложению для заказа такси

KEYWORDS = {
    "Usability (U)": ["интерфейс", "русском", "обучени", "касани", "тёмн"],
    "Reliability (R)": ["сбо", "обрыв", "сети", "сохран", "резерв"],
    "Performance (P)": ["секунд", "одновременн", "нагрузк", "отклик"],
    "Supportability (S)": ["модульн", "тест", "лог", "сервер", "конфигурац"],
    "+ (ограничения)": ["152-фз", "закон", "pci", "лицензи", "стандарт"],
    "Functionality (F)": ["заказ", "водител", "оплат", "уведомл", "тариф"],
}


def analyze_requirements(requirements_list):
    """Разносит требования по компонентам модели FURPS+ по ключевым словам."""
    result = {component: [] for component in KEYWORDS}
    result["Не классифицировано"] = []
    for requirement in requirements_list:
        text = requirement.lower()
        for component, words in KEYWORDS.items():
            if any(word in text for word in words):
                result[component].append(requirement)
                break  # требование отнесено к первому подошедшему компоненту
        else:
            result["Не классифицировано"].append(requirement)
    return result


REQUIREMENTS = [
    "Пассажир должен видеть положение водителя на карте в реальном времени",
    "Обновление позиции машины - каждые 5 секунд",
    "Интерфейс должен быть на русском языке, заказ - не более чем в 3 касания",
    "При обрыве сети активный заказ должен сохраняться",
    "Тарифы должны меняться на сервере без обновления приложения",
    "Обработка персональных данных - в соответствии с 152-ФЗ",
    "Приложение должно корректно масштабироваться на планшетах",
]

if __name__ == "__main__":
    for comp, reqs in analyze_requirements(REQUIREMENTS).items():
        print(comp + ":")
        for req in reqs:
            print("  -", req)
