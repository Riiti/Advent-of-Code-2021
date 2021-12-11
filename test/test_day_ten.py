from unittest.mock import patch

from aoc.challenges.day_10 import Syntax


def _mock_file():
    return Syntax(
        [
            "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]",
        ]
    )


@patch("aoc.challenges.day_10.Syntax.read_file", _mock_file)
def test_day_two_one():
    assert Syntax.read_file().part_one() == 26397


@patch("aoc.challenges.day_10.Syntax.read_file", _mock_file)
def test_day_two_two():
    assert Syntax.read_file().part_two() == 288957
