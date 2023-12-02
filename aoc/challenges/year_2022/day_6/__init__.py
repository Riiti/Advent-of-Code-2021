from aoc.helper.abstract import Challenge


def seperate_chars_slice(text: str, independent_chars: int) -> int:
    """Find the first occurence of four seperate chars"""
    for index in range(len(text) - (independent_chars - 1)):
        slice = set(text[index : index + independent_chars])
        if len(slice) == independent_chars:
            return index + independent_chars
    raise ValueError("No slice with four independent chars")


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> str:
        return data[0].strip()

    def part_one(self) -> int:
        return seperate_chars_slice(self.data, 4)

    def part_two(self) -> int:
        return seperate_chars_slice(self.data, 14)
