from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number("7000792289606361") == card_numbers

    assert get_mask_card_number("") == 0

def test_get_mask_account(mask_account):
    assert get_mask_account("73654108430135874305") == mask_account

    assert get_mask_account("sada") == 0
