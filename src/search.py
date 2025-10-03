import json
import os
import re

current_dir = os.path.dirname(__file__)
file = os.path.join(current_dir, "..", "data", "operations.json")


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь,
     в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    try:
        result_list = []
        for dict_ in data:
            description = dict_.get("description")
            if description:
                match = re.search(search, description, flags=re.IGNORECASE)
                if match:
                    result_list.append(dict_)
        return result_list

    except (KeyError, ValueError):
        return []


with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)
    # print(process_bank_search(data, 'Перевод организации'))
