"""
Working with 'csv' and 'json' structures.
Имеется файл cars.csv

Используйте библиотеку csv что бы прочитать содержимое файла.
Конвертируйте данные в формат json и сохраните в файл cars.json

Примечания:
•	используйте csv.DictReader
•	используйте json.dump с параметром indent=2
•	используйте контекстный менеджер with для создания файла

Check yourself:
bash$ cat ../task_23/cars.json
[
  {
    "Year": "1997",
    "Make": "Ford",
    "Model": "E350"
  },
  {
    "Year": "2000",
    "Make": "Mercury",
    "Model": "Cougar"
  },
  {
    "Year": "2006",
    "Make": "Dacia",
    "Model": "Logan"
  }
]
"""

import csv
import json


def read_csv():
    """read file data from csv file"""
    with open('cars.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        file_data = list(reader)
    return file_data


def write_json(data):
    """write json-formatted data in json file"""
    with open('cars.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == '__main__':
    csv_data = read_csv()
    write_json(csv_data)
