from aoc.challenges.year_2022.day_3 import Solver


def _mock_file():
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 157


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 70
