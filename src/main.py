import json
import os

from src.data_count import pd_data, pd_ex_data
from src.external_api import convert_transactions
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search

current_dir = os.path.dirname(__file__)
json_file_path = os.path.join(current_dir, "..", "data", "operations.json")
csv_file_path = os.path.join(current_dir, "..", "data", "transactions.csv")
xlsx_file_path = os.path.join(current_dir, "..", "data", "transactions_excel.xlsx")


def main():
    user_input = int(
        input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
                        Выберите необходимый пункт меню:\n
                        1. Получить информацию о транзакциях из JSON-файла\n
                        2. Получить информацию о транзакциях из CSV-файла\n
                        3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    )
    if user_input in [1, 2, 3]:
        if user_input == 1:
            print("Для обработки выбран JSON-файл")
            with open(json_file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                data_file = data
        elif user_input == 2:
            print("Для обработки выбран CSV-файл")
            data_file = pd_data(csv_file_path)
        elif user_input == 3:
            print("Для обработки выбран XLSX-файл")
            data_file = pd_ex_data(xlsx_file_path)
        filtered_data = []
        while True:
            input_status = input(
                """Введите статус, по которому необходимо выполнить фильтрацию.\n
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
            ).upper()
            if input_status in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Операции отфильтрованы по статусу {input_status}\n")
                filtered_data = filter_by_state(data_file, input_status)
                break  # выход из цикла
            else:
                print(f'Статус операции "{input_status}" недоступен\n')
                continue  # продолжить цикл для повторного ввода
        sort_answer = input("Отсортировать операции по дате? Да/Нет\n").lower()
        sorted_data = filtered_data
        if sort_answer == "да":
            answer = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if answer == "по возрастанию":
                sorted_data = sort_by_date(filtered_data)
            else:
                sorted_data = sort_by_date(filtered_data, reverse=True)
        rub_transaction = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if rub_transaction == "да":
            rub_res = convert_transactions(sorted_data)
        else:
            rub_res = sorted_data
        word_ans = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
        ).lower()
        if word_ans == "да":
            word = input("Слово: ")
            result = process_bank_search(rub_res, word)
            print("Программа:")
            print(f"Всего банковских операций в выборке: {len(result)}\n")

            for item in result:
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
                    currency = (
                        item["operationAmount"].get("currency", {}).get("name", "")
                    )

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

                print()
        else:
            print("Программа:")
            print(f"Всего банковских операций в выборке: {len(rub_res)}\n")

            for item in rub_res:
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
                    currency = (
                        item["operationAmount"].get("currency", {}).get("name", "")
                    )

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

                print()

    else:
        print("Введите номер желаемой операции.\n")


if __name__ == "__main__":
    main()
