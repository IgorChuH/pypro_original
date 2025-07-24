def get_date(data_main: str) -> str:
    just_date = data_main[: data_main.find("T")].split("-")
    just_date.reverse()
    return ".".join(just_date)


def mask_account_card(account_card: str) -> str:
    name_card = []
    number_card = []

    if account_card == "":
        return 0
    else:
        for i in account_card:
            if i == " " or i.isalpha():
                name_card.append(i)
            else:
                number_card.append(i)
        if "".join(name_card) == "Счет ":
            last_part = "".join(number_card[-4:])
            return f"{''.join(name_card)}**{last_part}"
        else:
            first_part = number_card[0:4]
            second_part = number_card[4:6] + ["**"]  # заменил на строчку ниже
            third_part = "*" * 4
            last_part = number_card[12:16]

            masked_name = "".join(name_card)
            masked_number = " ".join(
                [
                    "".join(first_part),
                    "".join(second_part),
                    third_part,
                    "".join(last_part),
                ]
            )

            return masked_name + masked_number
