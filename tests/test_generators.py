from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions, ex_transactions):
    usd_transactions = filter_by_currency(transactions, 'USD')
    without_cur = filter_by_currency(transactions)
    empty_dict = filter_by_currency([])

    assert (next(usd_transactions)) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert (next(usd_transactions)) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert (next(without_cur)) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }

    assert (next(without_cur)) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
    assert (next(empty_dict)) == 0




def test_transaction_descriptions(transactions, descriptions):
    usd_description = transaction_descriptions(transactions)
    empty_dict = transaction_descriptions([])
    assert (next(usd_description)) == 'Перевод организации'
    assert (next(usd_description)) == 'Перевод со счета на счет'
    assert (next(usd_description)) == 'Перевод со счета на счет'
    assert (next(usd_description)) == 'Перевод с карты на карту'
    assert (next(usd_description)) == 'Перевод организации'

    assert (next(empty_dict)) == 0
def test_card_number_generator():
    for card_number in card_number_generator(1, 5):
        print(card_number)
