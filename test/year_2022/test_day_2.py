from aoc.challenges.year_2022.day_2 import Solver


def _mock_file():
    return ["A Y", "B X", "C Z"]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 15


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 12
