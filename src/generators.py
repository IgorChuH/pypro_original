def filter_by_currency(transactions, currency="USD"):
    """
        Фильтрует транзакции по указанной валюте.

        Параметры:
        transactions (list): Список транзакций, каждая из которых должна быть словарём.
        currency (str): Код валюты для фильтрации, по умолчанию 'USD'.

        Возвращает:
        Генератор, который возвращает транзакции, соответствующие указанной валюте.
        Если список транзакций пуст, возвращает 0.
        """
    if transactions == ([]):
        yield 0

    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    """
        Извлекает описания транзакций.

        Параметры:
        transactions (list): Список транзакций, каждая из которых должна быть словарём.

        Возвращает:
        Генератор, который возвращает описания транзакций.
        Если список транзакций пуст, возвращает 0.
        """
    if transactions == ([]):
        yield 0
    else:
        for description in transactions:
            yield description["description"]

def card_number_generator(start: int, stop: int):
    """
        Генерирует номера карт в формате #### #### #### ####.

        Параметры:
        start (int): Начальное значение для генерации номеров карт.
        stop (int): Конечное значение для генерации номеров карт.

        Возвращает:
        Генератор строк, представляющих номера карт.
        Формат номеров состоит из 16 цифр, разделённых пробелами.
        """
    count = 0
    for generation in range(start, stop + 1):
        count += 1
        card_count = 16 - len(str(count))
        if card_count < 16:
            card_maker = "0" * card_count + str(count)
            result = card_maker[:4] + ' ' + card_maker[4:8] + ' ' + card_maker[8:12] + ' ' + card_maker[12:16]
            yield result





