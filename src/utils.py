import json
import logging
import os

current_dir = os.path.dirname(__file__)
file = os.path.join(current_dir, "..", "logs", "utils.log")
logger = logging.getLogger("transaction")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def input_transaction(filename: str):
    """Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла."""
    try:
        logger.info("Записываем данные в файл.")
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.info("Строка или поток не соответствует синтаксису JSON")
        logging.critical("Ошибка! Файл не найден.")
        return []
    except FileNotFoundError:
        logging.critical("Ошибка! Файл не найден.")
        return []


# data_str = input_transaction("../data/operations.json")
# print(data_str)
# print(type(data_str))

# for x in data_str:
# print(x["operationAmount"]["amount"])
