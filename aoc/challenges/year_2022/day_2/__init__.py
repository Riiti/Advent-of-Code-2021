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
    value: int = 0


class Scores:
    draw = 3
    lost = 0
    win = 6


encryption = {
    "A": Strategy(name=Options.Rock, value=1),
    "B": Strategy(name=Options.Paper, value=2),
    "C": Strategy(name=Options.Scissors, value=3),
    "X": Strategy(name=Options.Rock),
    "Y": Strategy(name=Options.Paper),
    "Z": Strategy(name=Options.Scissors),
}


def score(selections: list[tuple[Strategy, Strategy]]) -> int:
    scores = []
    for selection in selections:
        me, other = selection
        winner_score = find_winner(me.name, other.name)
        scores.append(me.value + winner_score)
    return sum(scores)


def find_winner(me: Options, other: Options) -> int:
    if me.Paper and other.Scissors:
        return Scores.lost
    elif me.Paper and other.Rock:
        return Scores.win
    elif me.Rock and other.Scissors:
        return Scores.win
    elif me.Rock and other.Paper:
        return Scores.lost
    elif me.Scissors and other.Rock:
        return Scores.win
    elif me.Scissors and other.Paper:
        return Scores.win
    return Scores.draw


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[tuple[Strategy, Strategy]]:
        selections = []
        for d in data:
            me, other = d.split()
            selections.append((encryption[me], encryption[other]))
        return selections

    def part_one(self) -> int:
        return score(self.data)

    def part_two(self) -> int:
        pass
