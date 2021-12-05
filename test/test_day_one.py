from unittest.mock import patch

import numpy as np

from aoc.challenges.day_1 import Sonar


def _mock_file():
    return Sonar(np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))


@patch("aoc.challenges.day_1.Sonar.read_file", _mock_file)
def test_day_one_one():
    assert Sonar.read_file().part_one() == 7


@patch("aoc.challenges.day_1.Sonar.read_file", _mock_file)
def test_day_one_two():
    assert Sonar.read_file().part_two() == 5
