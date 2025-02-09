import json
import os

from src.generators import transaction

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
# Задан путь к файлу с транзакциями в формате JSON

def read_json_file(path: str) -> list:
    """Функция, которая возвращает список словарей
    с данными о финансовых транзакциях из JSON-файла"""
    try:
        with open(path) as json_file:

            try:
                transactions_list = json.load(json_file)
            except json.JSONDecoderError:
                print("\nНевозможно декодировать JSON-данные")
                return []
    except FileNotFoundError:
        print("\nФайл не найден")
        return []
    else:
        if not transactions_list:
            print("\nФайл содержит пустой список")
            return []
        elif type(transactions_list) is not list:
            print("\nТип объекта в файле не список")
            return []
        return transactions_list

if __name__ == "__main__":
    print(read_json_file(PATH_TO_FILE))
