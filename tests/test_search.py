import unittest
from src.search import process_bank_search

class TestProcessBankSearch(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"description": "Оплата магазина"},
            {"description": "Перевод на карту"},
            {"description": "Оплата услуг"},
            {"description": "Пополнение счета"},
            {"description": None},
            {}
        ]

    def test_search_found(self):
        result = process_bank_search(self.data, "оплата")
        self.assertEqual(len(result), 2)
        self.assertTrue(all("оплата" in d.get("description", "").lower() for d in result))

    def test_search_case_insensitive(self):
        result = process_bank_search(self.data, "ПеРеВоД")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["description"], "Перевод на карту")

    def test_search_not_found(self):
        result = process_bank_search(self.data, "кредит")
        self.assertEqual(result, [])

    def test_missing_description(self):
        result = process_bank_search(self.data, "счет")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["description"], "Пополнение счета")

    def test_empty_data(self):
        result = process_bank_search([], "оплата")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()