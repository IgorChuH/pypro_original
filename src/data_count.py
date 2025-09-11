import csv
import os

import pandas as pd


def csv_data(__file__):
    """Функция, принимающая путь до csv-файла, считывает его и
    возвращающая список словарей с данными о
    финансовых транзакциях"""
    rows = []
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "..", "data", "transactions.csv")
    with open(file, encoding="utf-8", newline="") as res_file:
        reader = csv.DictReader(res_file, delimiter=";")
        for row in reader:
            # Если нужно — можно преобразовать типы полей здесь, например:
            # if 'amount' in row and row['amount']:
            #     row['amount'] = float(row['amount'].replace(',', '.'))
            rows.append(dict(row))
    return rows


# print(csv_data("C:\\Users\\ZIPHAI\\Decstop\\Testwork\\data\\transactions.csv"))


def pd_data(__file__):
    """Функция принимает путь до csv-файла, считывает его и возвращает список словарей с данными о финансовых транзакциях"""
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "..", "data", "transactions.csv")
    # при необходимости задайте encoding, sep, parse_dates и т.д.
    df = pd.read_csv(file, sep=";", encoding="utf-8")
    # преобразуем DataFrame в список словарей
    records = df.to_dict(orient="records")
    return records


print(pd_data("transactions.csv"))


def pd_ex_data(__file__):
    """Функция, принимающая путь до Excel-файла с помощью pandas, считывает его и
    возвращающая список словарей с данными о
    финансовых транзакциях"""
    current_dir = os.path.dirname(__file__)
    file = os.path.join(current_dir, "..", "data", "transactions_excel.xlsx")
    result_read_csv = pd.read_excel(file)
    return result_read_csv.head()


print(pd_ex_data("transactions_excel.xlsx"))
