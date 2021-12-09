from unittest.mock import patch

from aoc.challenges.day_9 import Lava


def _mock_file():
    return Lava(
        [
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 2, 1, 9, 9, 9, 4, 3, 2, 1, 0, 9],
            [9, 3, 9, 8, 7, 8, 9, 4, 9, 2, 1, 9],
            [9, 9, 8, 5, 6, 7, 8, 9, 8, 9, 2, 9],
            [9, 8, 7, 6, 7, 8, 9, 6, 7, 8, 9, 9],
            [9, 9, 8, 9, 9, 9, 6, 5, 6, 7, 8, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        ]
    )


@patch("aoc.challenges.day_9.Lava.read_file", _mock_file)
def test_day_two_one():
    assert Lava.read_file().part_one() == 15


@patch("aoc.challenges.day_9.Lava.read_file", _mock_file)
def test_day_two_two():
    assert Lava.read_file().part_two() == 1134
