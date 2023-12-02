from aoc.challenges.year_2022.day_6 import Solver


def _mock_file():
    return ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 10


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 29
