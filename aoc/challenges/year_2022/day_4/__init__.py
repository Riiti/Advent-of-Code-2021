from dataclasses import dataclass
from typing import Callable
from aoc.helper.abstract import Challenge


@dataclass
class Ranges:
    left: set[int]
    right: set[int]


def check_coverage(
    data: list[str], cov_func: Callable[[Ranges], bool]
) -> list[bool]:
    """Check if two ranges overlap"""
    matches = []
    for d in data:
        ranges = range_from_string(d)
        matches.append(cov_func(ranges))
    return matches


def range_from_string(range_str: str) -> Ranges:
    range_sets: list[set[int]] = []
    ranges = range_str.split(",")
    for ran in ranges:
        lower, upper = ran.split("-")
        range_sets.append(set(range(int(lower), int(upper) + 1)))
    return Ranges(*range_sets)


def range_covers_another(ranges: Ranges) -> bool:
    shared_items = len(ranges.left & ranges.right)
    return shared_items == len(ranges.left) or shared_items == len(ranges.right)


def partial_overlap(ranges: Ranges) -> bool:
    shared_items = len(ranges.left & ranges.right)
    return bool(shared_items)


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[str]:
        return [d.strip() for d in data]

    def part_one(self) -> int:
        return sum(check_coverage(self.data, range_covers_another))

    def part_two(self) -> int:
        return sum(check_coverage(self.data, partial_overlap))
