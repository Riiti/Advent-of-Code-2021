from aoc.challenges.year_2022.day_1 import Solver


def _mock_file():
    return [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
        "",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 24000


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 45000
