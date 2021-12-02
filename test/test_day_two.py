import numpy as np
import pandas as pd
import pytest
from unittest.mock import patch

from aoc.challenges.day_2 import Command


def _mock_file():
    return Command(
        pd.DataFrame(
            {
                "command": ["forward", "down", "forward", "up", "down", "forward"],
                "amount": [5, 5, 8, 3, 8, 2],
            }
        )
    )


@patch("aoc.challenges.day_2.Command.read_file", _mock_file)
def test_day_two_one():
    assert Command.read_file().part_one() == 150


@patch("aoc.challenges.day_2.Command.read_file", _mock_file)
def test_day_two_two():
    assert Command.read_file().part_two() == 900
