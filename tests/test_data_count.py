from io import StringIO
from unittest.mock import mock_open, patch

import pandas as pd

from src.data_count import csv_data, pd_data, pd_ex_data


def test_csv_data_reads_rows_using_csv_reader():
    # Подготовим содержимое "файла" с разделителем ;
    fake_file_content = "a;b;c\n1;2;3\nx;y;z\n"
    m_open = mock_open(read_data=fake_file_content)
    # Однако mock_open не всегда корректно работает с csv.reader (он ожидает итерируемый объект),
    # поэтому можно сделать так: patch builtins.open, возвращая StringIO напрямую
    with patch("builtins.open", return_value=StringIO(fake_file_content), create=True):
        with patch("csv.reader") as mock_csv_reader:
            # Настроим csv.reader так, чтобы он возвращал списки строк, как если бы правильно парсил
            mock_csv_reader.return_value = [
                ["a", "b", "c"],
                ["1", "2", "3"],
                ["x", "y", "z"],
            ]

            result = csv_data("dummy_path.csv")

            # Проверки
            mock_csv_reader.assert_called_once()  # csv.reader был вызван
            assert result == [
                ["a", "b", "c"],
                ["1", "2", "3"],
                ["x", "y", "z"],
            ]


def test_pd_data_calls_read_csv_and_returns_head():
    # Подготовим фиктивный DataFrame
    df = pd.DataFrame(
        {"col1": [1, 2, 3, 4, 5, 6], "col2": ["a", "b", "c", "d", "e", "f"]}
    )

    # Подменяем pd.read_csv, чтобы он возвращал наш DataFrame
    with patch("pandas.read_csv", return_value=df) as mock_read:
        result = pd_data("pandas.read_csv")

        # Проверяем, что pd.read_csv был вызван с нужными аргументами
        mock_read.assert_called_once_with("pandas.read_csv", sep=";")

        # Ожидаем, что функция вернула head() того DataFrame (по умолчанию 5 строк)
        expected = df.head()
        # Сравниваем содержимое: можно сравнить с помощью pandas.testing
        pd.testing.assert_frame_equal(result, expected)


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
