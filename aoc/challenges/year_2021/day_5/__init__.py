import re
from pathlib import Path
from typing import List, Tuple, Union

import numpy as np

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


def find_max(numbers: np.array) -> Tuple[int, int]:
    max_x = numbers[:, (0, 2)].max()
    max_y = numbers[:, (1, 3)].max()
    return (max_x, max_y)


def create_empty_map(max_x: int, max_y: int) -> np.array:
    return np.zeros((max_x + 2, max_y + 2))


def filter_coords(numbers: np.array) -> np.array:
    coords = numbers[
        ((numbers[:, 0] == numbers[:, 2]) | (numbers[:, 1] == numbers[:, 3]))
    ]
    return coords


def calc_missing_coords(line: np.array) -> List[Tuple[int, int]]:
    coords = check_for_diagonal(line)
    if coords:
        return coords
    x1, y1, x2, y2 = line
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    max_x, max_y = x2 - x1, y2 - y1
    x_cord = range(x1, x2) if max_x > 0 else [x1] * max_y
    y_cord = range(y1, y2) if max_y > 0 else [y1] * max_x
    return list(zip(x_cord, y_cord)) + [(x2, y2)]


def check_for_diagonal(
    line: np.array,
) -> Union[None, List[Tuple[int, int]]]:
    x1, y1, x2, y2 = line
    if abs(x1 - x2) == abs(y1 - y2):
        x_cord = range(x1, x2, 1) if x1 < x2 else range(x1, x2, -1)
        y_cord = range(y1, y2, 1) if y1 < y2 else range(y1, y2, -1)
        return list(zip(x_cord, y_cord)) + [(x2, y2)]


def create_connections(empty_map: np.array, numbers: np.array):
    for line in numbers:
        coords = calc_missing_coords(line)
        for coord in coords:
            empty_map[coord] += 1
    return empty_map


class Solver(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers

    @classmethod
    def read_file(cls) -> Challenge:
        number_regex = r"\d+"
        path = f"{Path(__file__).parent}/data/vents.txt"
        with open(path) as f:
            numbers = [re.findall(number_regex, lin) for lin in f.readlines()]
        return cls(np.array(numbers).astype(int))

    def part_one(self):
        self.filtered_numbers = filter_coords(self.numbers)
        max_x, max_y = find_max(self.filtered_numbers)
        empty_map = create_empty_map(max_x, max_y)
        empty_map = create_connections(empty_map, self.filtered_numbers)
        return np.count_nonzero(empty_map > 1)

    def part_two(self):
        max_x, max_y = find_max(self.numbers)
        empty_map = create_empty_map(max_x, max_y)
        empty_map = create_connections(empty_map, self.numbers)
        return np.count_nonzero(empty_map > 1)

    @staticmethod
    @day_wrapper
    def run():
        diag = Solver.read_file()
        print(f"More than one vent {diag.part_one()}.")
        print(f"More than one vent with diagonals {diag.part_two()}.")
