import csv

import pandas as pd


def csv_data(path_file):
    """Функция, принимающая путь до csv-файла, считывает его и
        возвращающая список словарей с данными о
        финансовых транзакциях"""
    result = []
    with open(path_file, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            result.append(row)
        return result


# print(csv_data("C:\\Users\\ZIPHAI\\Decstop\\Testwork\\data\\transactions.csv"))


def pd_data(path_file):
    """Функция, принимающая путь до csv-файла с помощью pandas, считывает его и
            возвращающая список словарей с данными о
            финансовых транзакциях"""
    result_read_csv = pd.read_csv(path_file, sep=";")
    return result_read_csv.head()


# print(pd_data("C:\\Users\\ZIPHAI\\Decstop\\Testwork\\data\\transactions.csv"))


def pd_ex_data(path_file):
    """Функция, принимающая путь до Excel-файла с помощью pandas, считывает его и
            возвращающая список словарей с данными о
            финансовых транзакциях"""
    result_read_csv = pd.read_excel(path_file)
    return result_read_csv.head()


print(pd_ex_data("C:\\Users\\ZIPHAI\\Decstop\\Testwork\\data\\transactions_excel.xlsx"))
