from aoc.helper.abstract import Challenge
import string

CHARS = string.ascii_lowercase + string.ascii_uppercase


def find_duplicate_chars(rucksack: str) -> int:
    first, second = split_string_in_half(rucksack)
    duplicate_char = set(first) & set(second)
    return CHARS.index(str(*duplicate_char)) + 1


def split_string_in_half(rucksack: str) -> tuple[str, str]:
    """Split a given string in the middle"""
    splitpoint = len(rucksack) // 2
    return rucksack[:splitpoint], rucksack[splitpoint:]


def find_common_char_in_chunk_of_three(rucksacks: list[str]) -> int:
    values = []
    for i in range(0, len(rucksacks[:-2]), 3):
        common_char = (
            set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])
        )
        values.append(CHARS.index(str(*common_char)) + 1)
    return sum(values)


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[str]:
        return [d.strip() for d in data]

    def part_one(self) -> int:
        return sum([find_duplicate_chars(rucksack) for rucksack in self.data])

    def part_two(self) -> int:
        return find_common_char_in_chunk_of_three(self.data)
