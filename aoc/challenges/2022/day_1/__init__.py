from aoc.helper.abstract import Challenge
from aoc.helper.filereader import read_file
from aoc.helper.wrapper import day_wrapper


class Solver(Challenge):
    def __init__(self, data: bytes) -> None:
        self.data = data

    def part_one(self) -> int:
        pass

    def part_two(self) -> int:
        pass


@day_wrapper
def run():
    data = read_file
    solver = Solver().read_file()
