# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as f: # Открываем файл в режиме чтения
        json_data = json.load(f) # Считываем данные из файла

    return round(sum([dict_["score"] * dict_["weight"] for dict_ in json_data]), 3)
    # Функция возвращает сумму произведений нужных значений по ключам из словарей
print(task())
