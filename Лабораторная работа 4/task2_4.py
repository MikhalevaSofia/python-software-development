# TODO импортировать необходимые молули
import csv # Импортирование модулей
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
      # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as f_csv: # Считывем содержимое csv файла с помощью DictReader
        lines = [line for line in csv.DictReader(f_csv)]


    with open(OUTPUT_FILENAME, "w") as f_json: # Открываем json файл на запись
        json.dump(lines, f_json, indent=4) # Сериализуем данные в файл
# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
