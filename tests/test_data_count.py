import io
import os
from unittest.mock import patch

import pandas as pd

from src.data_count import csv_data, pd_data, pd_ex_data

CSV_CONTENT = (
    "date;description;amount\n" "2021-01-01;Salary;1000\n" "2021-01-02;Coffee;-3.5\n"
)


def test_csv_data():
    mock_file = io.StringIO(CSV_CONTENT)
    with patch("src.data_count.open", return_value=mock_file):
        result = csv_data("dummy_path.csv")

    expected = [
        {"date": "2021-01-01", "description": "Salary", "amount": "1000"},
        {"date": "2021-01-02", "description": "Coffee", "amount": "-3.5"},
    ]
    assert result == expected


@patch("pandas.read_csv")
def test_pd_data(mock_read_csv):
    # Подготовка мок-DataFrame
    df = pd.DataFrame(
        data=[
            {"date": "2025-01-01", "amount": 100, "currency": "USD"},
            {"date": "2025-01-02", "amount": 200, "currency": "EUR"},
        ]
    )
    mock_read_csv.return_value = df

    fakefile = os.path.join("some", "path", "module.py")
    result = pd_data(fakefile)

    # Проверяем вызов pd.readcsv
    mock_read_csv.assert_called_once()
    called_path = mock_read_csv.call_args[0][0]
    expected_path = os.path.join(
        os.path.dirname(fakefile), "..", "data", "transactions.csv"
    )
    assert os.path.normpath(called_path), os.path.normpath(expected_path)

    # Проверяем переданные параметры
    kwargs = mock_read_csv.call_args[1]
    assert kwargs.get("sep"), ";"
    assert kwargs.get("encoding"), "utf-8"

    # Проверяем результат функции
    assert result, df.to_dict(orient="records")


@patch("pandas.read_excel")
def test_pd_ex_data(mock_read_excel):
    # Подготовка мок-DataFrame с более 3 строками
    df = pd.DataFrame(
        data=[
            {"date": "2025-01-01", "amount": 100},
            {"date": "2025-01-02", "amount": 200},
            {"date": "2025-01-03", "amount": 300},
            {"date": "2025-01-04", "amount": 400},
        ]
    )
    mock_read_excel.return_value = df

    fakefile = os.path.join("some", "path", "module.py")
    result = pd_ex_data(fakefile)

    # Проверяем вызов pd.readexcel
    mock_read_excel.assert_called_once()
    called_path = mock_read_excel.call_args[0][0]
    expected_path = os.path.join(
        os.path.dirname(fakefile), "..", "data", "transactions_excel.xlsx"
    )
    assert os.path.normpath(called_path), os.path.normpath(expected_path)

    # pdexdata возвращает head() DataFrame — сверяем с ожидаемым
    assert result, df.head()
