from aoc.challenges.year_2022.day_7 import Solver


def _mock_file():

    return [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]


def test_day_one_one():
    solver = Solver(_mock_file())
    assert solver.part_one() == 95437


def test_day_one_two():
    solver = Solver(_mock_file())
    assert solver.part_two() == 24933642
