from copy import deepcopy
from collections import defaultdict
import re
from typing import Any
from aoc.helper.abstract import Challenge

SEPERATING_CHAR = "\n"


def fill_pillars(containers: list[str]) -> dict[int, list[str]]:
    """Build pillars from data input"""
    coll = defaultdict(list[str])
    [
        coll[group.start() // 4 + 1].append(group.group())
        for container in containers[::-1]
        for group in [*re.finditer(r"[\w]", container)]
    ]
    return dict(coll)


def extract_instructions(instructions: list[str]) -> list[tuple[int, int, int]]:
    return [
        tuple(int(num) for num in re.findall(r"\d+", inst))
        for inst in instructions
    ]


def reorder_columns(
    pillars: dict[int, list[str]], instructions: list[Any], inverse: bool = True
) -> dict[int, list[str]]:
    pill = deepcopy(pillars)
    order = -1 if inverse else 1
    for inst in instructions:
        (quantity, source, goal) = inst
        items_to_switch = pill[source][-int(quantity) :]
        pill[source] = pill[source][: -int(quantity)]
        pill[goal].extend(items_to_switch[::order])
    return pill


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.pillars, self.instructions = self.preprocess(data)

    def preprocess(
        self, data: list[str]
    ) -> tuple[dict[int, list[str]], list[Any]]:
        sep_line = data.index(SEPERATING_CHAR)
        containers = data[: sep_line - 1]
        instructions = data[sep_line + 1 :]
        pillars = fill_pillars(containers)
        ext_insts = extract_instructions(instructions)
        return pillars, ext_insts

    def part_one(self) -> str:
        pillars = reorder_columns(self.pillars, self.instructions)
        return "".join(pill[-1] for pill in pillars.values())

    def part_two(self) -> str:
        pillars = reorder_columns(
            self.pillars, self.instructions, inverse=False
        )
        return "".join(pill[-1] for pill in pillars.values())
