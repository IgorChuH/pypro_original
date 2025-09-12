import logging
import os

current_dir = os.path.dirname(__file__)
file = os.path.join(current_dir, '..', 'logs', 'mask.log')
logger = logging.getLogger("mask")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    file, mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number):
    if card_number.isdigit() and len(card_number) == 16:
        logger.info("Началась шифровка вашей карты.")
        first_part = card_number[0:4]
        second_part = card_number[4:6] + "**"
        third_part = "*" * 4
        last_part = card_number[12:16]
        logger.info("Номер карты зашифрован.")
        return first_part + " " + second_part + " " + third_part + " " + last_part
    else:
        logger.critical("Данные введены некорректно.")
        return 0


def get_mask_account(account_number):
    if account_number.isdigit():
        logger.info("Началась шифровка вашего номера аккаунта.")
        last_part = account_number[-4:]
        logger.info("Номер аккаунта зашифрован.")
        return f"**{last_part}"
    else:
        logger.critical("Данные введены некорректно.")
        return 0
