import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(account_card):
    assert mask_account_card("Visa Platinum 7000792289606361") == account_card

    assert mask_account_card("") == "Неподходящий формат для ввода."


def test_get_date(date):
    assert get_date("2024-03-11T02:26:18.671407") == date

    assert get_date("2023-12-11T02:26:18.671407") == "11.12.2023"


@pytest.mark.parametrize(
    "account_card, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_par_account_card(account_card, expected_result):
    assert mask_account_card(account_card) == expected_result
