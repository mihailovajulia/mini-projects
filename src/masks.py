def get_mask_card_number(card_number: str) -> str:
    """Функция, которая возвращает маску номера карты"""
    if len(card_number) != 16:
        raise ValueError("Неверная длина номера карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(bank_account: str) -> str:
    """Функция, которая возвращает маску номера счета"""
    if (8 <= len(bank_account) < 20):
        raise ValueError("Неверная длина номера счета")
    return f"**{bank_account[-4:]}"
