def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску номера карты"""
    return f"{card_number[:4]} {card_number[6:8]}** **** {card_number[12:]}"


def get_mask_account(bank_account: str) -> str:
    """Функция, которая возвращает маску номера счета"""
    return f"{'*' * 2}{bank_account[-4:]}"
