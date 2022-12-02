from dataclasses import dataclass
from enum import Enum
from aoc.helper.abstract import Challenge


class Options(Enum):
    Rock = "Rock"
    Paper = "Paper"
    Scissors = "Scissors"


@dataclass
class Strategy:
    name: Options
    value: int


class Scores:
    draw = 3
    lost = 0
    win = 6


Rock = Strategy(name=Options.Rock, value=1)
Paper = Strategy(name=Options.Paper, value=2)
Scissors = Strategy(name=Options.Scissors, value=3)


moves = {
    "X": Rock,
    "Y": Paper,
    "Z": Scissors,
    "A": Rock,
    "B": Paper,
    "C": Scissors,
}


goals = {"X": Scores.lost, "Y": Scores.draw, "Z": Scores.win}


def score(selections: list[tuple[str, str]]) -> int:
    scores = []
    for selection in selections:
        me, other = moves[selection[0]], moves[selection[1]]
        winner_score = find_winner(me.name, other.name)
        scores.append(me.value + winner_score)
    return sum(scores)


def find_winner(me: Options, other: Options) -> int:
    scores = {
        (Options.Paper, Options.Scissors): Scores.lost,
        (Options.Paper, Options.Rock): Scores.win,
        (Options.Rock, Options.Scissors): Scores.win,
        (Options.Rock, Options.Paper): Scores.lost,
        (Options.Scissors, Options.Rock): Scores.lost,
        (Options.Scissors, Options.Paper): Scores.win,
    }
    return scores.get((me, other), Scores.draw)


def find_move(selections: list[tuple[str, str]]) -> int:
    scores = []
    for selection in selections:
        other = moves[selection[1]]
        goal = goals[selection[0]]
        me = move_mapping(other, goal)
        scores.append(me.value + goal)
    return sum(scores)


def move_mapping(other: Strategy, goal: int) -> Strategy:
    mapping = {
        (Options.Rock, Scores.win): Paper,
        (Options.Paper, Scores.win): Scissors,
        (Options.Scissors, Scores.win): Rock,
        (Options.Rock, Scores.lost): Scissors,
        (Options.Paper, Scores.lost): Rock,
        (Options.Scissors, Scores.lost): Paper,
    }
    return mapping.get((other.name, goal), other)


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[tuple[str, str]]:
        selections = []
        for d in data:
            other, me = d.split()
            selections.append((me, other))
        return selections

    def part_one(self) -> int:
        return score(self.data)

    def part_two(self) -> int:
        return find_move(self.data)
