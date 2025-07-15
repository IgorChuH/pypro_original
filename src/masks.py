def get_mask_card_number(card_number):
    if card_number.isdigit() and len(card_number) == 16:
        first_part = card_number[0:4]
        second_part = card_number[4:6] + "**"
        third_part = "*" * 4
        last_part = card_number[12:16]
        return f"({first_part} {second_part} {third_part} {last_part})"


def get_mask_account(account_number):
    if account_number.isdigit():
        last_part = account_number[-4:]
        return f"**{last_part}"
