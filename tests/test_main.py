import json
import unittest
from unittest.mock import mock_open, patch

from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search


class TestBankTransactions(unittest.TestCase):

    def setUp(self):
        # Установка mock-данных для тестов
        self.mock_data = [
            {
                "id": 879660146,
                "state": "EXECUTED",
                "date": "2018-07-22T07:42:32.953324",
                "operationAmount": {
                    "amount": "92130.50",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 19628854383215954147",
                "to": "Счет 90887717138446397473",
            },
            {
                "id": 893507143,
                "state": "EXECUTED",
                "date": "2018-02-03T07:16:28.366141",
                "operationAmount": {
                    "amount": "90297.21",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
                "description": "Открытие вклада",
                "to": "Счет 37653295304860108767",
            },
            {
                "id": 710136990,
                "state": "CANCELED",
                "date": "2018-08-17T03:57:28.607101",
                "operationAmount": {
                    "amount": "66906.45",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Maestro 1913883747791351",
                "to": "Счет 11492155674319392427",
            },
        ]

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([]))
    def test_load_json(self, mock_file):
        with open("dummy_path.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [])

    def test_filter_by_state(self):
        filtered_data = filter_by_state(self.mock_data, "EXECUTED")
        self.assertEqual(len(filtered_data), 2)
        self.assertIn(self.mock_data[0], filtered_data)
        self.assertIn(self.mock_data[1], filtered_data)

    def test_sort_by_date(self):
        sorted_data = sort_by_date(self.mock_data)
        # Проверьте, что данные отсортированы корректно
        self.assertEqual(
            sorted_data[0]["date"], "2018-02-03T07:16:28.366141"
        )  # Открытие вклада
        self.assertEqual(
            sorted_data[1]["date"], "2018-07-22T07:42:32.953324"
        )  # Перевод организации
        self.assertEqual(
            sorted_data[2]["date"], "2018-08-17T03:57:28.607101"
        )  # Перевод организации (Canceled)

    def test_process_bank_search(self):
        result = process_bank_search(self.mock_data, "Перевод организации")
        self.assertEqual(len(result), 2)  # Убедитесь, что найдено два элемента
        descriptions = [item["description"] for item in result]
        self.assertIn("Перевод организации", descriptions)


if __name__ == "__main__":
    unittest.main()
