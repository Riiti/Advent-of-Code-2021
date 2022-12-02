from aoc.challenges.year_2021.day_3 import Solver


def _mock_file():
    return [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]


def test_day_two_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 198


def test_day_two_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 230
