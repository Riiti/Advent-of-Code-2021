from functools import lru_cache
from pathlib import Path
from typing import List

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


@lru_cache
def solve_with_recursion(days_till_spawn: int, days: int) -> int:
    """Calculates how many fish are spwaned by every lanternfish"""
    if days_till_spawn >= days:
        return 1
    if days_till_spawn == 0:
        return solve_with_recursion(8, days - 1) + solve_with_recursion(
            6, days - 1
        )
    else:
        return solve_with_recursion(days_till_spawn - 1, days - 1)


class Solver(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers

    @classmethod
    def read_file(cls) -> Challenge:
        path = f"{Path(__file__).parent}/data/lanternfish.txt"
        with open(path) as f:
            numbers = f.read().split(",")
        return cls(numbers)

    def part_one(self) -> int:
        return sum([solve_with_recursion(int(n), 80) for n in self.numbers])

    def part_two(self) -> int:
        return sum([solve_with_recursion(int(n), 256) for n in self.numbers])

    @staticmethod
    @day_wrapper
    def run():
        fish = Solver.read_file()
        print(f"After 80 days there are {fish.part_one()} fish in the sea.")
        print(f"After 256 days there are {fish.part_two()} fish in the sea.")
