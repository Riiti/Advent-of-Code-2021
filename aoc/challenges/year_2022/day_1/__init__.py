from aoc.helper.abstract import Challenge


def sum_chunks(data: list[str]) -> list[int]:
    """Calc the sum over numbers till the first empty string is found"""
    sums = []
    sum = 0
    for calories in data:
        try:
            sum += int(calories)
        except ValueError:
            sums.append(sum)
            sum = 0
    return sums


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[str]:
        return [d.strip() for d in data]

    def part_one(self) -> int:
        return max(sum_chunks(self.data))

    def part_two(self) -> int:
        return sum(sorted(sum_chunks(self.data), reverse=True)[:3])
