import unittest
from src.process_operations import process_bank_operations

class TestProcessBankOperations(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"description": "Оплата"},
            {"description": "оплата"},
            {"description": "Перевод"},
            {"description": "оплата"},
            {"description": None},
            {},  # отсутствует поле description
            {"description": "Перевод"}
        ]
        self.categories = ["Оплата", "Перевод", "Покупка"]

    def test_count_operations(self):
        result = process_bank_operations(self.data, self.categories)
        self.assertEqual(result["Оплата"], 3)   # 3 раза "оплата" (регистр игнорируется)
        self.assertEqual(result["Перевод"], 2)  # 2 раза "перевод"
        self.assertEqual(result["Покупка"], 0)  # нет совпадений

    def test_empty_data(self):
        result = process_bank_operations([], self.categories)
        self.assertEqual(result, {cat: 0 for cat in self.categories})

    def test_empty_categories(self):
        result = process_bank_operations(self.data, [])
        self.assertEqual(result, {})

    def test_case_insensitivity(self):
        custom_categories = ["оплата", "ПеРеВоД"]
        result = process_bank_operations(self.data, custom_categories)
        # Ключи возвращаются в исходном регистре, поэтому проверяем именно их
        self.assertEqual(result["оплата"], 3)
        self.assertEqual(result["ПеРеВоД"], 2)

if __name__ == "__main__":
    unittest.main()