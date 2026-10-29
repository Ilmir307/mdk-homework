# Анализ и применение стандартов кодирования в системах контроля версий

**МДК 02.02 · группа 3424А**
**Репозиторий:** [github.com/Ilmir307/pep8-git-demo](https://github.com/Ilmir307/pep8-git-demo) · **Pull request:** [#1](https://github.com/Ilmir307/pep8-git-demo/pull/1)

## 1. Цель работы

Изучить стандарт PEP 8 и применить его в работе с системой контроля версий Git: настроить инструменты форматирования, зафиксировать нарушения в отдельной ветке, исправить их и провести слияние через pull request с ревью.

## 2. Основные правила PEP 8 (использованные в работе)

- имена функций и переменных — в snake_case, констант — в UPPER_CASE;
- 4 пробела на отступ, две пустые строки между функциями верхнего уровня;
- пробелы вокруг операторов и после запятых, без пробелов у скобок вызова;
- строки не длиннее 79 символов; у модуля и каждой функции — docstring.

## 3. Настройка репозитория и инструментов форматирования

Создан репозиторий `pep8-git-demo` на GitHub. Инструменты форматирования настраиваются файлом [pyproject.toml](https://github.com/Ilmir307/pep8-git-demo/blob/main/pyproject.toml):

```toml
[tool.black]
line-length = 79

[tool.autopep8]
max_line_length = 79
```

Проверка соответствия выполняется инструментами `pycodestyle` (оформление) и `pylint` (качество кода).

## 4. Процесс работы с Git

1. Инициализирован репозиторий, в основную ветку `main` добавлены `main.py` и `pyproject.toml`.
2. Создана ветка разработки `feature/pep8-violations`.
3. В ветке закоммичена функция `calc_sum`, намеренно нарушающая PEP 8.
4. `git status` подтвердил чистое состояние после коммита: `On branch feature/pep8-violations, nothing to commit, working tree clean`.
5. Проверка выявила нарушения (лог — в файле [1556-pycodestyle-log.txt](1556-pycodestyle-log.txt)):

```text
main.py:8:1: E302 expected 2 blank lines, found 1
main.py:8:14: E201 whitespace after '('
main.py:8:16: E231 missing whitespace after ','
main.py:8:18: E202 whitespace before ')'
main.py:9:9: E117 over-indented
main.py:9:15: E225 missing whitespace around operator
main.py:12:1: E305 expected 2 blank lines after class or function definition, found 1
main.py:14:11: E201 whitespace after '('
main.py:14:22: E231 missing whitespace after ','
main.py:14:25: E202 whitespace before ')'
```

6. Все нарушения исправлены и зафиксированы отдельным коммитом; повторная проверка: `pycodestyle` — чисто, `pylint` — 10.00/10, программа выводит `Привет, мир!` и `3`.
7. Ветка отправлена на GitHub, создан pull request [#1](https://github.com/Ilmir307/pep8-git-demo/pull/1) с описанием проделанного.
8. Проведено ревью: в PR оставлен комментарий о соответствии стандартам (snake_case, пробелы, пустые строки, отступы). Замечаний нет — выполнено слияние в `main`.

Итоговая история (`git log --oneline`):

```text
80eebff Merge pull request #1 from Ilmir307/feature/pep8-violations
ae1218d Исправлены нарушения PEP 8 (E201, E202, E225, E231, E302, E305, E117)
65f665d WIP: функция calc_sum (с нарушениями PEP 8)
b54dce6 Добавлен main.py и конфигурация black/autopep8 (pyproject.toml)
```

## 5. Вывод

Стандарт PEP 8 применён в полном рабочем цикле Git: настройка инструментов форматирования через `pyproject.toml`, разработка в отдельной ветке, обнаружение нарушений инструментом `pycodestyle`, исправление отдельным коммитом и слияние через pull request с ревью. Такой процесс гарантирует, что в основную ветку попадает только код, прошедший проверку стандартов, а история нарушений и исправлений остаётся видимой в репозитории.
