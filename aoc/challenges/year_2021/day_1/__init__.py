from aoc.helper.abstract import Challenge


def previous_bigger_than_current(data: list[int]) -> list[bool]:
    """Check if current element of list is bigger than the previous"""
    elements = []
    for index, current in enumerate(data[1:]):
        previous = data[index]
        elements.append(current > previous)
    return elements


def sliding_window(data: list[int]) -> list[int]:
    """Calculate the sliding window over 3 elements"""
    window_sums = []
    for index in range(len(data) - 2):
        sum = data[index] + data[index + 1] + data[index + 2]
        window_sums.append(sum)
    return window_sums


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[int]:
        return [int(d) for d in data]

    def part_one(self) -> int:
        return sum(previous_bigger_than_current(self.data))

    def part_two(self) -> int:
        window_sums = sliding_window(self.data)
        return sum(previous_bigger_than_current(window_sums))
