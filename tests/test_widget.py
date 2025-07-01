import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize('input_mask, output_mask', [
                         ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                          ('Счет 73654108430135874305', 'Счет **4305'),
                          ('', 'Неверный формат данных')
])
def test_mask_account_card(input_mask, output_mask):
    assert mask_account_card(input_mask) == output_mask

@pytest.mark.parametrize('input_mask, output_mask', [
                         ('2024-03-11T02:26:18.671407', '11.03.2024'),
                          ('', 'Неверный формат даты')
])

def test_get_date(input_mask, output_mask):
    assert get_date(input_mask) == output_mask
