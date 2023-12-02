from aoc.challenges.year_2022.day_5 import Solver
from aoc.challenges.year_2022.day_5 import SEPERATING_CHAR


def _mock_file():

    return [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
        SEPERATING_CHAR,
        "move 1 from 2 to 1 ",
        "move 3 from 1 to 3 ",
        "move 2 from 2 to 1 ",
        "move 1 from 1 to 2 ",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == "CMZ"


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == "MCD"
