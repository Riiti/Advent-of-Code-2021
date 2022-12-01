from aoc.helper.abstract import Challenge
from aoc.helper.filereader import read_file
from aoc.helper.wrapper import day_wrapper


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[int]:
        pass

    def part_one(self) -> int:
        pass

    def part_two(self) -> int:
        pass


@day_wrapper
def run():
    data = read_file("data/data.txt")
    breakpoint()
    solver = Solver(data)


run()
