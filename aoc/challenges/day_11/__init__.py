from pathlib import Path
from typing import List

import numpy as np

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper

ADJECENT = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def recursive_solver(
    map: np.array, iteration: int = 0, stop_con: int = 100, count=0
):
    if iteration == stop_con:
        return count

    map[1:-1, 1:-1] += 1
    map, flashes = add_adjacent(map, 0)
    return recursive_solver(map, iteration + 1, stop_con, count + flashes)


def add_adjacent(light_map: np.array, count: int) -> np.array:
    map_wo_border = light_map[1:-1, 1:-1]
    coords = np.argwhere([map_wo_border > 9])
    if len(coords) == 0:
        return light_map, count
    for _, y, x in coords:
        # Add one to account for the border
        y += 1
        x += 1
        light_map[y, x] = 0
        for off_x, off_y in ADJECENT:
            if light_map[y + off_y, x + off_x] != 0:
                light_map[y + off_y, x + off_x] += 1
    return add_adjacent(light_map, count + len(coords))


class Lights(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers

    @classmethod
    def read_file(cls) -> Challenge:
        path = f"{Path(__file__).parent}/data/lights.txt"
        nums = []
        with open(path) as f:
            for line in f.readlines():
                nums.append([n for n in line.strip()])
        return cls(
            np.pad(
                np.array(nums).astype(int),
                1,
                mode="constant",
                constant_values=0,
            )
        )

    def part_one(self) -> int:
        print(recursive_solver(self.numbers))

    def part_two(self) -> int:
        pass

    @staticmethod
    @day_wrapper
    def run():
        syn = Lights.read_file()
        print(f"Lights score {syn.part_one()}.")
        print(f"Missing brackets score {syn.part_two()}.")


print(Lights.read_file().part_one())
