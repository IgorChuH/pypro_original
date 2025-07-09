from masks import get_mask_account, get_mask_card_number

def get_date(data_main: str) -> str:
    just_date = data_main[:data_main.find("T")].split('-')
    just_date.reverse()
    return '.'.join(just_date)

def mask_account_card(account_card: str) -> str:
    name_card = []
    number_card = []

    for i in account_card:
        if i.isalpha():
            name_card.append(i)
        else:
            number_card.append(i)
    if name_card == 'Счёт':
        return name_card + " " + get_mask_account(number_card)
    else:
        return name_card + " " + get_mask_card_number(number_card)

print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
"""
    first_part = number_card[0:4]
    second_part = number_card[4:6] + ["**"]
    third_part = "*" * 4
    last_part = number_card[12:16]

    masked_name = ''.join(name_card)
    masked_number = ' '.join([
        ''.join(first_part),
        ''.join(second_part),
        third_part,
        ''.join(last_part)
    ])

    return masked_name + ' ' + masked_number"""
