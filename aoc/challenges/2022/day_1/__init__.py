from pathlib import Path


from aoc.helper.abstract import Challenge
from aoc.helper.wrapper import day_wrapper


class Calories(Challenge):
    def part_one(self) -> int:
        return np.sum(np.where(self.values[:-1] < self.values[1:], 1, 0))

    def part_two(self) -> int:
        window_sum = self.values[:-2] + self.values[1:-1] + self.values[2:]
        return np.sum(np.where(window_sum[:-1] < window_sum[1:], 1, 0))


@day_wrapper
def run():
    solver = Calories().read_file()
    print(f"Values larger than the previous {sonar.part_one()}.")
    print(
        f"Values larger than the previous in sliding window of three {sonar.part_two()}."
    )
