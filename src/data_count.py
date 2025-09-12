import csv
import os

import pandas as pd

current_dir = os.path.dirname(__file__)
file_csv = os.path.join(current_dir, "..", "data", "transactions.csv")
file_ex = os.path.join(current_dir, "..", "data", "transactions_excel.xlsx")


def csv_data(path_file):
    """Функция, принимающая путь до csv-файла, считывает его и
    возвращающая список словарей с данными о
    финансовых транзакциях"""
    rows = []
    path = os.path.normpath(os.path.abspath(path_file))
    with open(path, encoding="utf-8", newline="") as res_file:
        reader = csv.DictReader(res_file, delimiter=";")
        for row in reader:
            # Если нужно — можно преобразовать типы полей здесь, например:
            # if 'amount' in row and row['amount']:
            #     row['amount'] = float(row['amount'].replace(',', '.'))
            rows.append(dict(row))
    return rows


print(csv_data(file_csv))


def pd_data(path_file):
    """Функция принимает путь до csv-файла, считывает его и возвращает список словарей с данными о финансовых транзакциях"""
    # при необходимости задайте encoding, sep, parse_dates и т.д.
    df = pd.read_csv(path_file, sep=";", encoding="utf-8")
    # преобразуем DataFrame в список словарей
    records = df.to_dict(orient="records")
    return records


print(pd_data(file_csv))


def pd_ex_data(path_file):
    """Функция, принимающая путь до Excel-файла с помощью pandas, считывает его и
    возвращающая список словарей с данными о
    финансовых транзакциях"""
    result_read_csv = pd.read_excel(path_file)
    return result_read_csv.head()


print(pd_ex_data(file_ex))
