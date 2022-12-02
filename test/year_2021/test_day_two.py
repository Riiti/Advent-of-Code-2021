from aoc.challenges.year_2021.day_2 import Solver


def _mock_file():
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]


def test_day_two_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 150


def test_day_two_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 900
