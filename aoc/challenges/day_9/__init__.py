import math
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


def find_lowest(num):
    smallest = []
    for y in range(1, len(num) - 1):
        for x in range(1, len(num[0]) - 1):
            if num[y][x] < min(
                [num[y - 1][x], num[y + 1][x], num[y][x - 1], num[y][x + 1]]
            ):
                smallest.append(num[y][x])
    return smallest


def find_basin(num) -> int:

    y_range = range(1, len(num) - 1)
    x_range = range(1, len(num[0]) - 1)

    num = low_waterlevel(num, y_range, x_range, initial=True)
    num = low_waterlevel(num, y_range[::-1], x_range)
    num = low_waterlevel(num, y_range, x_range[::-1])
    num = low_waterlevel(num, y_range[::-1], x_range[::-1])

    return calc_count(num, x_range, y_range)


def low_waterlevel(
    num: List, y_range: range, x_range: range, initial: bool = False
):
    spacer = 10
    for y in y_range:
        for x in x_range:
            surrrounding = [
                num[y - 1][x],
                num[y + 1][x],
                num[y][x - 1],
                num[y][x + 1],
            ]
            if max(surrrounding) > 9 and num[y][x] != 9:
                num[y][x] = max(surrrounding)
            elif max(surrrounding) <= 9 and num[y][x] != 9 and initial:
                num[y][x] = spacer
                spacer += 1
    return num


def calc_count(num: Dict, x_range: range, y_range: range) -> int:
    count = defaultdict(int)
    for y in y_range:
        for x in x_range:
            count[num[y][x]] += 1
    return math.prod(
        sorted([value for key, value in count.items() if key != 9])[-3:]
    )


class Lava(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers

    @classmethod
    def read_file(cls) -> Challenge:
        path = f"{Path(__file__).parent}/data/lava.txt"
        lava = []
        with open(path) as f:
            for line in f.readlines():
                lava.append([9] + [int(num) for num in line.strip()] + [9])
        lava = [[9] * (len(line) + 2), *lava, [9] * (len(line) + 2)]
        return cls(lava)

    def part_one(self) -> int:
        values = find_lowest(self.numbers)
        return sum([val + 1 for val in values])

    def part_two(self) -> int:
        return find_basin(self.numbers)

    @staticmethod
    @day_wrapper
    def run():
        lava = Lava.read_file()
        print(f"Lava lowspots {lava.part_one()}.")
        print(f"Digits encoding {lava.part_two()}.")
