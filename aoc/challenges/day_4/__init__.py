import re
from pathlib import Path
from typing import List, Union

import numpy as np

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


def check_axis(field: np.array, number: List) -> int:
    for i in range(5):
        # Check rows
        row_values = field[i, :]
        in_row = [field_number in number for field_number in row_values]

        # Check columns
        column_values = field[:, i]
        in_column = [field_number in number for field_number in column_values]
        if any((all(in_row), all(in_column))):
            return calc_stat(field, number)


def field_to_numbers(fields: List) -> List[List[int]]:
    number_regex = r"\d{1,2}"
    for field in fields:
        yield np.array(re.findall(number_regex, field)).reshape(5, 5).astype(
            int
        )


def calc_stat(field: np.array, numbers: List) -> int:
    last_num = numbers[-1]
    arr = field[~np.isin(field, numbers)].sum()
    return arr * last_num


class Field:
    def __init__(
        self, numbers: np.array, fields: np.array, solved: np.array
    ) -> None:
        self.numbers = numbers
        self.fields = fields
        self.solved = solved

    def check_fields(self, index: int, first: bool = True) -> Union[int, List]:
        numbers = self.numbers[:index]
        for i, field in enumerate(self.fields):
            found = check_axis(field, numbers)
            if found:
                self.solved[i] = 1
                if first:
                    return found
                if all(self.solved):
                    return found


class Bingo(Challenge):
    def __init__(self, numbers: List, fields: List[np.array]) -> None:
        self.numbers = numbers
        self.fields = fields
        self.solved = [0] * len(self.fields)

    @classmethod
    def read_file(cls):
        path = f"{Path(__file__).parent}/data/bingo.txt"
        with open(path) as f:
            blocks = f.read().split("\n\n")
            numbers = [int(num) for num in blocks[0].split(",")]
            fields = [*field_to_numbers(blocks[1:])]
        return cls(numbers, fields)

    def part_one(self):
        field = Field(self.numbers, self.fields, self.solved)
        for index in range(5, len(self.numbers)):
            value = field.check_fields(index)
            if value:
                return value

    def part_two(self):
        field = Field(self.numbers, self.fields, self.solved)
        for index in range(5, len(self.numbers)):
            value = field.check_fields(index, first=False)
            if value:
                return value

    @staticmethod
    @day_wrapper
    def run():
        diag = Bingo.read_file()
        print(f"Bingo Score to win: {diag.part_one()}.")
        print(f"Last board to win: {diag.part_two()}.")
