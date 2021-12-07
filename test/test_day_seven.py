from unittest.mock import patch

from aoc.challenges.day_7 import Whales


def _mock_file():
    return Whales([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])


@patch("aoc.challenges.day_7.Whales.read_file", _mock_file)
def test_day_two_one():
    assert Whales.read_file().part_one() == 37


@patch("aoc.challenges.day_7.Whales.read_file", _mock_file)
def test_day_two_two():
    assert Whales.read_file().part_two() == 168
