from pathlib import Path
from typing import List

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


def calc_fuel(data: list, threshold: int, inconsistent: bool = False):
    if inconsistent:
        return sum(
            [inconsitent_fuel(abs(int(y) - int(threshold))) for y in data]
        )
    return sum([abs(int(y) - int(threshold)) for y in data])


def inconsitent_fuel(fuel: int) -> int:
    return fuel * (fuel + 1) // 2


class Solver(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers
        self.levels = range(min(self.numbers), max(self.numbers))

    @classmethod
    def read_file(cls) -> Challenge:
        path = f"{Path(__file__).parent}/data/whales.txt"
        with open(path) as f:
            numbers = f.read().split(",")
        return cls([int(num) for num in numbers])

    def part_one(self) -> int:

        return min(calc_fuel(self.numbers, n) for n in self.levels)

    def part_two(self) -> int:
        return min(
            calc_fuel(self.numbers, n, inconsistent=True) for n in self.levels
        )

    @staticmethod
    @day_wrapper
    def run():
        fish = Solver.read_file()
        print(f"Fuel of crabs {fish.part_one()}.")
        print(f"Fuel of inconsistent {fish.part_two()}.")
