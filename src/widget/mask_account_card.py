def mask_account_card(account_card):
    name_card = []
    number_card = []

    for i in account_card:
        if i.isalpha():
            name_card.append(i)
        else:
            number_card.append(i)

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

    return masked_name + ' ' + masked_number


result = mask_account_card("Visa Platinum 7000792289606361")
print(result)