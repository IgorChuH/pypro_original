import json
import os

import requests
from dotenv import load_dotenv

current_dir = os.path.dirname(__file__)
file = os.path.join(current_dir, "..", "data", "operations.json")

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_transactions(filename: list[dict]):
    """Принимает список транзакций и возвращает список сумм в рублях,
    приводя валюты USD и EUR к RUB через внешний API."""
    try:
        result = []
        for i in filename:
            if i["operationAmount"]["currency"]["code"] == "RUB":
                res_amount = i["operationAmount"]["amount"]
                result.append(res_amount)

            elif (
                i["operationAmount"]["currency"]["code"] == "USD"
                or i["operationAmount"]["currency"]["code"] == "EUR"
            ):
                amount = i["operationAmount"]["amount"]
                if i["operationAmount"]["currency"]["code"] == "USD":
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={amount}"
                    payload = {}
                    headers = {"apikey": f"{API_KEY}"}
                    response = requests.get(url, headers=headers, data=payload)
                    status_code = response.status_code
                    if status_code == 200:
                        convert_amount = response.json()
                        res_amount = convert_amount["result"]
                        result.append(res_amount)
                    else:
                        return "Произошла ошибка сервера"
                elif i["operationAmount"]["currency"]["code"] == "EUR":
                    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={amount}"
                    payload = {}
                    headers = {"apikey": f"{API_KEY}"}
                    response = requests.get(url, headers=headers, data=payload)
                    status_code = response.status_code
                    if status_code == 200:
                        convert_amount = response.json()
                        res_amount = convert_amount["result"]
                        result.append(res_amount)
                    else:
                        return "Произошла ошибка сервера"
        return result
    except requests.exceptions.RequestException:
        return "An error occurred. Please try again later."


if __name__ == "__main__":

    with open(file, "r", encoding="utf-8") as file:
        data = json.load(file)
    print(convert_transactions(data))
