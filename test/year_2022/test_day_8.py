from aoc.challenges.year_2022.day_8 import Solver


def _mock_file():

    return [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 21


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 8
