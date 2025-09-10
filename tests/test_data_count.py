import io
from unittest.mock import mock_open, patch

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


@patch('pandas.read_csv')
def test_pd_data_success(mock_read_csv):
    # Подготовим фиктивный DataFrame
    df_mock = pd.DataFrame([
        {'date': '2021-01-01', 'amount': 100, 'category': 'food'},
        {'date': '2021-01-02', 'amount': 200, 'category': 'rent'},
    ])
    # Настроим mock возвращать наш DataFrame
    mock_read_csv.return_value = df_mock

    # Вызов функции
    result = pd_data('dummy_path.csv')

    # Проверки
    mock_read_csv.assert_called_once_with('dummy_path.csv', sep=';', encoding='utf-8')
    expected = df_mock.to_dict(orient='records')
    assert result == expected


def test_pd_ex_data_calls_read_excel_and_returns_head():
    # Подготовим реальный DataFrame
    df = pd.DataFrame(
        {"col1": [1, 2, 3, 4, 5, 6], "col2": ["a", "b", "c", "d", "e", "f"]}
    )

    # Патчим pandas.read_excel в пространстве имён модуля, где используется pd
    with patch("pandas.read_excel", return_value=df) as mock_read:
        result = pd_ex_data("dummy_path.xlsx")

        # Проверяем вызов read_excel без указания sep
        mock_read.assert_called_once_with("dummy_path.xlsx")

        # Ожидаем, что функция вернула head() (по умолчанию 5 строк)
        expected = df.head()
        pd.testing.assert_frame_equal(result, expected)
