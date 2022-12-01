import statistics
from pathlib import Path
from typing import List

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper

CORR_CHAR = {"(": ")", "[": "]", "{": "}", "<": ">"}


def count_occurences(syntax: str, calc_return: bool = False) -> int:
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    opens = []
    for char in syntax:
        if char in CORR_CHAR.keys():
            opens = [CORR_CHAR[char]] + opens
        elif char in CORR_CHAR.values():
            if char != opens[0]:
                if calc_return:
                    return 0
                return score[char]
            opens.remove(char)
    if not calc_return:
        return 0
    return calc_score(opens)


def calc_score(missing: List) -> int:
    vals = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for miss in missing:
        score *= 5
        score += vals[miss]
    return score


class Solver(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers

    @classmethod
    def read_file(cls) -> Challenge:
        path = f"{Path(__file__).parent}/data/syntax.txt"
        with open(path) as f:
            syntax = f.read().split("\n")
        return cls(syntax)

    def part_one(self) -> int:
        return sum([count_occurences(syn) for syn in self.numbers])

    def part_two(self) -> int:
        vals = [count_occurences(sy, calc_return=True) for sy in self.numbers]
        return statistics.median([val for val in vals if val != 0])

    @staticmethod
    @day_wrapper
    def run():
        syn = Solver.read_file()
        print(f"Syntax score {syn.part_one()}.")
        print(f"Missing brackets score {syn.part_two()}.")


print(Solver.read_file().part_two())
