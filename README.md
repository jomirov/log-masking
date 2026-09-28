## Цель задачи

Создание утилиты для удаления значений чувствительных полей с сохранением полезных сведений о событии. Требования:
- Написание функции redact, которая возвращает новую структуру с замаскированными значениями
- Обработка локального файла input.json и сохранение результата в output.json с режимом предварительного просмотра
- Добавление четырех проверок через unittest и запуск в Github Actions

## Запуск утилиты
```powershell
py main.py
```
### Пример входящих данных
```json
{
    "event": "login",
    "email": "anna@example.test",
    "token": "demo123",
    "meta": {
        "EMAIL": "bob@example.test",
        "attempt": 2
    },
    "items": [
        {"token": "demo456"}
    ],
    "message": "user entered"
}
```
### Итоговые данные
Значения ключей email и token маскируются без учёта регистра
```json
{
    "event": "login",
    "email": "[HIDDEN]",
    "token": "[HIDDEN]",
    "meta": {
        "EMAIL": "[HIDDEN]",
        "attempt": 2
    },
    "items": [
        {"token": "[HIDDEN]"}
    ],
    "message": "user entered"
}
```
## Запуск тестов
```powershell
py test_redact.py
```