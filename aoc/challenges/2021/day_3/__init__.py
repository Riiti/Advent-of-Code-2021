from pathlib import Path

import numpy as np
import pandas as pd

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


def recursive_solver(data: np.array, index: int = 0, co_scrub: bool = False):
    if len(data) == 1:
        return int("".join(str(bina) for bina in data[0]), 2)

    # Calculate the mean to see which number is more frequent
    mean = np.mean(data[:, index])
    mean = 1 if mean == 0.5 else int(mean.round(0))
    if not co_scrub:
        mean = 1 - mean
    data = data[data[:, index] == mean]

    # Recureivly calculate data
    return recursive_solver(data, index=(index + 1), co_scrub=co_scrub)


class Diagnostik(Challenge):
    def __init__(self, frame: pd.DataFrame) -> None:
        self.values = frame

    def part_one(self):
        median = np.median(self.values, axis=0).astype(int)
        gamma = int("".join(str(med) for med in median), 2)
        epsilon = int("".join(str(1 - med) for med in median), 2)
        return gamma * epsilon

    def part_two(self):
        oxygen_gen = recursive_solver(self.values, index=0, co_scrub=True)
        co_scrubber = recursive_solver(self.values, index=0, co_scrub=False)
        return oxygen_gen * co_scrubber

    @classmethod
    def read_file(cls):
        path = f"{Path(__file__).parent}/data/diagnostics.txt"
        with open(path) as f:
            data = [[int(x) for x in line.strip()] for line in f.readlines()]
        return cls(np.array(data))

    @staticmethod
    @day_wrapper
    def run():
        diag = Diagnostik.read_file()
        print(f"Power consumption of Submarine is {diag.part_one()}.")
        print(f"Life support rating is {diag.part_two()}.")
