import numpy as np

from aoc.helper.abstract import Challenge


def recursive_solver(data: np.ndarray, index: int = 0, co_scrub: bool = False):
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


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> np.ndarray:
        values = [[int(x) for x in num] for num in data]
        return np.array(values)

    def part_one(self):
        median = np.median(self.data, axis=0).astype(int)
        gamma = int("".join(str(med) for med in median), 2)
        epsilon = int("".join(str(1 - med) for med in median), 2)
        return gamma * epsilon

    def part_two(self):
        oxygen_gen = recursive_solver(self.data, index=0, co_scrub=True)
        co_scrubber = recursive_solver(self.data, index=0, co_scrub=False)
        return oxygen_gen * co_scrubber
