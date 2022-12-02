from aoc.challenges.year_2021.day_1 import Solver


def _mock_file():
    return [
        "199",
        "200",
        "208",
        "210",
        "200",
        "207",
        "240",
        "269",
        "260",
        "263",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 7


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 5
