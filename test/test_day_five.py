from unittest.mock import patch

import numpy as np

from aoc.challenges.day_5 import Sonar


def _mock_file():
    return Sonar(
        np.array(
            [
                [0, 9, 5, 9],
                [8, 0, 0, 8],
                [9, 4, 3, 4],
                [2, 2, 2, 1],
                [7, 0, 7, 4],
                [6, 4, 2, 0],
                [0, 9, 2, 9],
                [3, 4, 1, 4],
                [0, 0, 8, 8],
                [5, 5, 8, 2],
            ]
        )
    )


@patch("aoc.challenges.day_5.Sonar.read_file", _mock_file)
def test_day_two_one():
    assert Sonar.read_file().part_one() == 5


@patch("aoc.challenges.day_5.Sonar.read_file", _mock_file)
def test_day_two_two():
    assert Sonar.read_file().part_two() == 12
