from numpy.core.records import array
import pandas as pd
import numpy as np
import re

from pathlib import Path
from typing import List, Union
from aoc.helper.abstract import Challenge

from aoc.helper.wrapper import day_wrapper


class Diagnostik(Challenge):
    def __init__(self, numbers: List, fields: List[np.array]) -> None:
        self.numbers = numbers
        self.fields = fields

    def part_one(self):
        for index in range(5, len(self.numbers)):
            value = self.check_fields(index)
            if value:
                return value

    def part_two(self):
        for index in range(5, len(self.numbers)):
            wins = self.check_fields(index)
            if wins:
                last_win = wins
        return last_win

    @classmethod
    def read_file(cls):
        path = f"{Path(__file__).parent}/data/bingo.txt"
        with open(path) as f:
            blocks = f.read().split("\n\n")
            numbers = [int(num) for num in blocks[0].split(",")]
            fields = [*Diagnostik.field_to_numbers(blocks[1:])]
        return cls(numbers, fields)

    @staticmethod
    def field_to_numbers(fields: List) -> List[List[int]]:
        number_regex = "\d{1,2}"
        for field in fields:
            yield np.array(re.findall(number_regex, field)).reshape(5, 5).astype(int)

    def check_fields(self, index: int, first: bool = True) -> Union[int, List]:
        found = False
        numbers = self.numbers[:index]
        for field in self.fields:
            found = Diagnostik.check_axis(field, numbers)
            if found and first:
                return found
        return found

    @staticmethod
    def check_axis(field: np.array, number: List, axis: int = 0) -> int:
        for i in range(5):
            # Check rows
            row_values = field[i, :]
            in_row = [field_number in number for field_number in row_values]

            # Check columns
            column_values = field[:, i]
            in_column = [field_number in number for field_number in column_values]
            if any((all(in_row), all(in_row))):
                return Diagnostik.calc_stat(field, number)

    @staticmethod
    def calc_stat(field: np.array, numbers: List) -> int:
        last_num = numbers[-1]
        arr = field[~np.isin(field, numbers)].sum()
        return arr * last_num

    @staticmethod
    @day_wrapper
    def run():
        diag = Diagnostik.read_file()
        print(f"Power consumption of Submarine is {diag.part_one()}.")
        print(f"Life support rating is {diag.part_two()}.")


print(Diagnostik.read_file().part_one())
print(Diagnostik.read_file().part_two())
