# Анализ качества кода с использованием статического анализатора Pylint

**МДК 02.02 · группа 3424А**

## 1. Цель работы

Изучить и применить статический анализатор Pylint для анализа качества кода: выявить проблемы в предоставленном фрагменте кода, исправить их и проверить результат повторным анализом.

**Инструмент:** Pylint 4.0.9 (Python 3.12). Запуск: `python -m pylint <файл>`.

## 2. Анализируемый фрагмент кода

Файл [task1600_original.py](task1600_original.py) — учебный фрагмент с типичными нарушениями стандартов кодирования:

```python
class product:
    def __init__(self,Name,Price):
        self.Name=Name
        self.Price=Price

    def getPrice(self):
        return self.Price

def Calc_total(items):
    total=0
    for i in items:
        total=total+i.getPrice()
    unused_variable = 5
    return total

MyList = [product("Хлеб",50),product("Молоко",80)]
print("Итого: " + str(Calc_total(MyList)))
```

## 3. Первичный запуск Pylint

```text
C0114: Missing module docstring (missing-module-docstring)
C0115: Missing class docstring (missing-class-docstring)
C0103: Class name "product" doesn't conform to PascalCase naming style
C0103: Attribute name "Name" doesn't conform to snake_case naming style
C0103: Attribute name "Price" doesn't conform to snake_case naming style
C0103: Argument name "Name" doesn't conform to snake_case naming style
C0103: Argument name "Price" doesn't conform to snake_case naming style
C0116: Missing function or method docstring (getPrice)
C0103: Method name "getPrice" doesn't conform to snake_case naming style
R0903: Too few public methods (1/2) (too-few-public-methods)
C0116: Missing function or method docstring (Calc_total)
C0103: Function name "Calc_total" doesn't conform to snake_case naming style
C0103: Constant name "MyList" doesn't conform to UPPER_CASE naming style

Your code has been rated at 0.71/10
```

## 4. Таблица выявленных проблем и исправлений

| № | Проблема (код Pylint) | Описание | Исправление |
|---|---|---|---|
| 1 | C0114 missing-module-docstring | У модуля нет строки документации | Добавлен docstring модуля с описанием назначения |
| 2 | C0115 missing-class-docstring | У класса нет документации | Добавлен docstring класса |
| 3 | C0103 invalid-name (class) | Имя класса `product` не в стиле PascalCase | Переименовано в `Product` |
| 4 | C0103 invalid-name (attribute) | Атрибуты `Name`, `Price` не в snake_case | Переименованы в `name`, `price` |
| 5 | C0103 invalid-name (argument) | Аргументы `Name`, `Price` не в snake_case | Переименованы в `name`, `price` |
| 6 | C0116 missing-function-docstring | У метода `getPrice` нет документации | Добавлен docstring метода |
| 7 | C0103 invalid-name (method) | Имя метода `getPrice` в camelCase вместо snake_case | Переименовано в `get_price` |
| 8 | R0903 too-few-public-methods | У класса только один публичный метод | Добавлен полезный метод `apply_discount` (скидка в процентах) |
| 9 | C0116 missing-function-docstring | У функции `Calc_total` нет документации | Добавлен docstring функции |
| 10 | C0103 invalid-name (function) | Имя функции `Calc_total` не в snake_case | Переименована в `calc_total` |
| 11 | C0103 invalid-name (constant) | `MyList` на верхнем уровне воспринимается как константа, а имя не в UPPER_CASE | Код перенесён в блок `if __name__ == "__main__":`, переменная переименована в `my_list` |

Дополнительно при исправлении: однобуквенная переменная цикла `i` заменена на говорящее `item`, а вокруг операторов добавлены пробелы по PEP 8.

## 5. Исправленный код

Файл [task1600_fixed.py](task1600_fixed.py) — все проблемы устранены, добавлены docstring, имена приведены к соглашениям PEP 8, логика работы не изменена (проверено запуском: программа выводит `Итого: 130`).

## 6. Повторный запуск Pylint

```text
Your code has been rated at 10.00/10
```

## 7. Вывод

Pylint применён для статического анализа учебного фрагмента кода: при первичном запуске выявлено 13 замечаний (оценка 0.71/10) — отсутствие документации (C0114–C0116), нарушения соглашений об именовании PEP 8 (C0103: PascalCase для классов, snake_case для функций и переменных) и недостаточный интерфейс класса (R0903). Все замечания исследованы и исправлены; повторный анализ дал оценку **10.00/10**. Практическая польза инструмента очевидна: Pylint автоматически отлавливает то, что при ручном ревью пропускают, — единый стиль имён и отсутствие документации.
