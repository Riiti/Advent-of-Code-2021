from pathlib import Path

import numpy as np

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


class Solver(Challenge):
    def __init__(self, array: np.array) -> None:
        self.values = array

    def part_one(self) -> int:
        return np.sum(np.where(self.values[:-1] < self.values[1:], 1, 0))

    def part_two(self) -> int:
        window_sum = self.values[:-2] + self.values[1:-1] + self.values[2:]
        return np.sum(np.where(window_sum[:-1] < window_sum[1:], 1, 0))

    @classmethod
    def read_file(cls):

        path = f"{Path(__file__).parent}/data/sonar_values.txt"
        with open(path) as f:
            data = [int(line) for line in f.readlines()]
        return cls(np.array(data))

    @staticmethod
    @day_wrapper
    def run():
        sonar = Solver.read_file()
        print(f"Values larger than the previous {sonar.part_one()}.")
        print(
            f"Values larger than the previous in sliding window of three {sonar.part_two()}."
        )
