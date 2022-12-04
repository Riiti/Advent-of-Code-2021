from aoc.challenges.year_2022.day_4 import Solver


def _mock_file():
    return [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 2


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 4
