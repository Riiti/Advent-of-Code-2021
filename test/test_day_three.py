from unittest.mock import patch

import numpy as np

from aoc.challenges.day_3 import Diagnostik


def _mock_file():
    return Diagnostik(
        np.array(
            [
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0],
            ]
        )
    )


@patch("aoc.challenges.day_3.Diagnostik.read_file", _mock_file)
def test_day_two_one():
    assert Diagnostik.read_file().part_one() == 198


@patch("aoc.challenges.day_3.Diagnostik.read_file", _mock_file)
def test_day_two_two():
    assert Diagnostik.read_file().part_two() == 230
