from unittest.mock import patch

import numpy as np

from aoc.challenges.day_11 import Lights


def _mock_file():
    return Lights(
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 5, 4, 8, 3, 1, 4, 3, 2, 2, 3, 0],
                [0, 2, 7, 4, 5, 8, 5, 4, 7, 1, 1, 0],
                [0, 5, 2, 6, 4, 5, 5, 6, 1, 7, 3, 0],
                [0, 6, 1, 4, 1, 3, 3, 6, 1, 4, 6, 0],
                [0, 6, 3, 5, 7, 3, 8, 5, 4, 7, 8, 0],
                [0, 4, 1, 6, 7, 5, 2, 4, 6, 4, 5, 0],
                [0, 2, 1, 7, 6, 8, 4, 1, 7, 2, 1, 0],
                [0, 6, 8, 8, 2, 8, 8, 1, 1, 3, 4, 0],
                [0, 4, 8, 4, 6, 8, 4, 8, 5, 5, 4, 0],
                [0, 5, 2, 8, 3, 7, 5, 1, 5, 2, 6, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
    )


@patch("aoc.challenges.day_11.Lights.read_file", _mock_file)
def test_day_two_one():
    assert Lights.read_file().part_one() == 1656


@patch("aoc.challenges.day_11.Lights.read_file", _mock_file)
def test_day_two_two():
    assert Lights.read_file().part_two() == 195
