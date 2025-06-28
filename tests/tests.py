def get_mask_card_number(card_number):
    """
    Маскирует номер кредитной карты, открывая только определенные части.

    Аргументы:
        card_number (str): 16-значный номер кредитной карты.

    Возвращает:
        str: Замаскированный номер карты в формате (xxxx xx** **** xxxx).
    """
    if card_number.isdigit() and len(card_number) == 16:
        first_part = card_number[0:4]
        second_part = card_number[4:6] + "**"
        third_part = "*" * 4
        last_part = card_number[12:16]
        return f"({first_part} {second_part} {third_part} {last_part})"
    return "Неверный номер карты"

def get_mask_account(account_number):
    """
    Маскирует номер счета, открывая только последние четыре цифры.

    Аргументы:
        account_number (str): Номер счета в виде строки.

    Возвращает:
        str: Замаскированный номер счета в формате **xxxx.
    """
    if account_number.isdigit():
        last_part = account_number[-4:]
        return f'**{last_part}'
    return "Неверный номер счета"

print(get_mask_card_number("1234567891231111"))
print(get_mask_account("1234567891231111"))