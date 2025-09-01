import json


def input_transaction(filename: str):
    """Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []


# data_str = input_transaction("../data/operations.json")
# print(data_str)
# print(type(data_str))

# for x in data_str:
# print(x["operationAmount"]["amount"])
