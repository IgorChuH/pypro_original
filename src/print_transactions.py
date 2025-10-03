
def print_output(data: list[dict]) -> None:
    """
    Выводит список банковских операций в формате:

    Программа:
    Всего банковских операций в выборке: X

    Дата Описание
    Откуда -> Куда
    Сумма: сумма валюта

    Пример драйвера для использования:
    print_transactions(result)
    """

    print("Программа:")
    print(f"Всего банковских операций в выборке: {len(data)}\n")

    for item in data:
        date = item.get("date", "")
        description = item.get("description", "")
        from_ = ""
        to_ = ""
        amount = ""
        currency = ""

        # Извлечение информации о счетах и сумме
        if "from" in item:
            from_ = item["from"]
        if "to" in item:
            to_ = item["to"]
        if "operationAmount" in item:
            amount = item["operationAmount"].get("amount", "")
            currency = item["operationAmount"].get("currency", {}).get("name", "")

        # Форматируем вывод для счетов/карт
        # Если from и to есть, то выводим строку "from -> to"
        # Иначе, если из описания можно вытащить "Счет **4321" или аналогично, можно добавить кастомизацию
        print(f"{date} {description}")

        if from_ and to_:
            print(f"{from_} -> {to_}")
        elif from_:
            print(from_)
        elif to_:
            print(to_)

        if amount and currency:
            print(f"Сумма: {amount} {currency}")
        else:
            print("Сумма: не указана")

        print()  # пустая строка для разделения операций
