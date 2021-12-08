from unittest.mock import patch

from aoc.challenges.day_8 import Digits


def _mock_file():
    return Digits(
        [
            [
                [
                    "be",
                    "cfbegad",
                    "cbdgef",
                    "fgaecd",
                    "cgeb",
                    "fdcge",
                    "agebfd",
                    "fecdb",
                    "fabcd",
                    "edb",
                ],
                ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
            ]
        ]
    )


@patch("aoc.challenges.day_8.Digits.read_file", _mock_file)
def test_day_two_one():
    assert Digits.read_file().part_one() == 2


@patch("aoc.challenges.day_8.Digits.read_file", _mock_file)
def test_day_two_two():
    assert Digits.read_file().part_two() == 8394
