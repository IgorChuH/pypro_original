import unittest
from unittest.mock import Mock, patch

import requests

from src.external_api import convert_transactions


class TestConvertTransactions(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_rub_amount_keeps_as_is(self, mock_get):
        data = [{"operationAmount": {"amount": "100.50", "currency": {"code": "RUB"}}}]
        # requests.get не должен вызываться для RUB
        res = convert_transactions(data)
        self.assertEqual(res, ["100.50"])
        mock_get.assert_not_called()

    @patch("src.external_api.requests.get")
    def test_usd_conversion_success(self, mock_get):
        data = [{"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}]
        # Подготовим мок-ответ
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"result": 780.0}
        mock_get.return_value = mock_resp

        res = convert_transactions(data)
        self.assertEqual(res, [780.0])
        # Проверим, что вызван правильный URL
        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]
        self.assertIn("from=USD", called_url)
        self.assertIn("to=RUB", called_url)
        self.assertIn("amount=10", called_url)

    @patch("src.external_api.requests.get")
    def test_eur_conversion_success(self, mock_get):
        data = [{"operationAmount": {"amount": "5", "currency": {"code": "EUR"}}}]
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"result": 450.0}
        mock_get.return_value = mock_resp

        res = convert_transactions(data)
        self.assertEqual(res, [450.0])
        mock_get.assert_called_once()
        called_url = mock_get.call_args[0][0]
        # В вашей функции URL для EUR сейчас ошибочный (from=USD). Тест ожидает from=EUR.
        self.assertIn("from=EUR", called_url)

    @patch("src.external_api.requests.get")
    def test_api_server_error(self, mock_get):
        data = [{"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}]
        mock_resp = Mock()
        mock_resp.status_code = 500
        mock_get.return_value = mock_resp

        res = convert_transactions(data)
        self.assertEqual(res, "Произошла ошибка сервера")

    @patch("src.external_api.requests.get")
    def test_request_exception_handled(self, mock_get):
        data = [{"operationAmount": {"amount": "1", "currency": {"code": "USD"}}}]
        mock_get.side_effect = requests.exceptions.RequestException
        res = convert_transactions(data)
        self.assertEqual(res, "An error occurred. Please try again later.")


if __name__ == "__main__":
    unittest.main()
