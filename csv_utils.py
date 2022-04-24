import csv
from typing import List



def write_file(*, file_to_write: str, fields: List, rows: List[List]):
    with open(file_to_write, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)


def read_file(*, file_to_read: str):
    rows = []
    with open(file_to_read, 'r+') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)
    return fields, rows


def add_by_position(*, rows: List, position=None, new_row: List):
    if isinstance(new_row, list):
        if position is not None:
            rows.insert(position, new_row)
        else:
            rows.append(new_row)
    else:
        print("Please, enter list")
    return rows


def delete_by_position(*, rows: List, position=None):
    if position is not None:
        rows.pop(position)
    else:
        rows.pop()
    return rows


def count_sum(*, file_to_read: str):
    with open(file_to_read, 'r') as file_count:
        csv_sum = csv.reader(file_count, delimiter=';')
        dist = 0
        for row in csv_sum:
            _dist = row[1]
            try:
                _dist = int(_dist)
            except ValueError:
                _dist = 0

            dist += _dist

        print(f'Общая сумма всех товаров = {dist} $')



















