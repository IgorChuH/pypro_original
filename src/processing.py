from datetime import datetime


def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """
    Фильтрует список словарей по указанному состоянию.

    Параметры:
    list_of_dict (list): Список словарей для фильтрации.
    state (str): Состояние, по которому нужно фильтровать (по умолчанию "EXECUTED").

    Возвращает:
    list: Список словарей с указанным состоянием.
    """
    filtered_list = []
    for directory in list_of_dict:
        if directory.get("state") == state:
            filtered_list.append(directory)
    return filtered_list


def sort_by_date(list_of_dict: list, reverse=False):
    """
    Сортирует список словарей по дате.

    Параметры:
    list_of_dict (list): Список словарей для сортировки.
    reverse (bool): Если True, сортировка по убыванию (по умолчанию True).

    Возвращает:
    list: Отсортированный список словарей.
    """
    try:
        return sorted(
            list_of_dict,
            key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
            reverse=reverse,
        )
    except (KeyError, ValueError):
        return 0
