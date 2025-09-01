import json
import unittest
from unittest.mock import mock_open, patch

# импортируем тестируемую функцию
from src.utils import input_transaction


class TestInputTransaction(unittest.TestCase):

    def test_returns_list_for_valid_json_list(self):
        data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        m = mock_open(read_data=json.dumps(data))
        with patch("builtins.open", m), patch("json.load", side_effect=json.load):
            result = input_transaction("dummy.json")
        self.assertEqual(result, data)

    def test_returns_empty_list_for_empty_file(self):
        # пустой файл -> json.load вызовет JSONDecodeError
        m = mock_open(read_data="")
        with patch("builtins.open", m):
            with patch(
                "json.load", side_effect=json.JSONDecodeError("msg", doc="", pos=0)
            ):
                result = input_transaction("dummy.json")
        self.assertEqual(result, [])

    def test_returns_empty_list_for_file_not_found(self):
        # открытие файла вызывает FileNotFoundError
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = input_transaction("no_such_file.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
