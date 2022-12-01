from pathlib import Path
from typing import Dict, List

from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper

UNIQUE_VALUES = {2: 1, 4: 4, 3: 7, 7: 8}


def check_match(output: List) -> int:
    return sum([1 for num in output if len(num) in UNIQUE_VALUES.keys()])


def get_unique_number(input: List) -> Dict:
    unique = {
        UNIQUE_VALUES[len(num)]: num
        for num in input
        if len(num) in UNIQUE_VALUES.keys()
    }
    six_nine_zero = [chars for chars in input if len(chars) == 6]
    two_three_five = [chars for chars in input if len(chars) == 5]

    unique[3] = "".join(extract_by_diff(two_three_five, unique[1], 2))
    unique[6] = "".join(extract_by_diff(six_nine_zero, unique[1], 1))
    unique[2], unique[5] = extract_last_two(
        two_three_five, unique[3], unique[4], 2
    )
    unique[0], unique[9] = extract_last_two(
        six_nine_zero, unique[6], unique[3], 4
    )
    return {"".join(sorted(v)): k for k, v in unique.items()}


def extract_by_diff(nums: List, one: str, diff: int):
    return [num for num in nums if len(set(num) & set(one)) == diff]


def extract_last_two(nums: List, known: str, diff: str, schwelle: int):
    nums = [num for num in nums if num != known]
    if len(set(nums[0]) & set(diff)) == schwelle:
        return "".join(nums[0]), "".join(nums[1])
    return "".join(nums[1]), "".join(nums[0])


def string_to_number(output: List, mapping: Dict) -> int:
    return int("".join([str(mapping["".join(sorted(key))]) for key in output]))


class Solver(Challenge):
    def __init__(self, numbers: List) -> None:
        self.numbers = numbers

    @classmethod
    def read_file(cls) -> Challenge:
        path = f"{Path(__file__).parent}/data/digits.txt"
        displays = []
        with open(path) as f:
            for line in f.readlines():
                input, output = line.split("|")
                input = input.split()
                output = output.split()
                displays.append([input, output])
        return cls(displays)

    def part_one(self) -> int:
        return sum([check_match(output) for input, output in self.numbers])

    def part_two(self) -> int:
        sum = 0
        for input, output in self.numbers:
            mapping = get_unique_number(input)
            sum += string_to_number(output, mapping)
        return sum

    @staticmethod
    @day_wrapper
    def run():
        fish = Solver.read_file()
        print(f"Digits {fish.part_one()}.")
        print(f"Digits encoding {fish.part_two()}.")
