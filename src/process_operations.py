import json
import os
from collections import Counter

current_dir = os.path.dirname(__file__)
file = os.path.join(current_dir, "..", "data", "operations.json")


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Принимает список словарей операций и список категорий.
    Возвращает словарь {category: count} для каждой указанной категории.
    Сравнение категорий и поля 'description' нечувствительно к регистру.
    """
    result_dict = []

    #    for item in categories:
    #        for i in data:
    #          value = i.get("description")
    #           result_dict.append()
    norm_to_orig = {cat.lower(): cat for cat in categories}
    counts = {cat: 0 for cat in categories}

    # Собираем все описания транзакций в нормализованном виде
    descriptions = (
        (item.get("description") or "").lower()
        for item in data
        if isinstance(item, dict)
    )

    desc_counter = Counter(descriptions)

    # Для каждой заданной категории берём количество по точному совпадению
    for norm, orig in norm_to_orig.items():
        counts[orig] = desc_counter.get(norm, 0)

    return counts


categories = ["Перевод организации", "Перевод со счета на счет", "Открытие вклада"]


with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
    # print(process_bank_operations(data, categories))
