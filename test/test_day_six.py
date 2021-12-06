from unittest.mock import patch

from aoc.challenges.day_6 import Lanternfish


def _mock_file():
    return Lanternfish([3, 4, 3, 1, 2])


@patch("aoc.challenges.day_6.Lanternfish.read_file", _mock_file)
def test_day_two_one():
    assert Lanternfish.read_file().part_one() == 5934


@patch("aoc.challenges.day_6.Lanternfish.read_file", _mock_file)
def test_day_two_two():
    assert Lanternfish.read_file().part_two() == 26984457539
