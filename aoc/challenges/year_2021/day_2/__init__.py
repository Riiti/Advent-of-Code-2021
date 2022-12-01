from dataclasses import dataclass
from enum import Enum


from aoc.helper.abstract import Challenge


class Comand(Enum):
    forward = "forward"
    down = "down"
    up = "up"


@dataclass
class Instruction:
    direction: Comand
    value: int


def value_by_field(instructions: list[Instruction], field: Comand) -> int:
    """Calculate the sum of steps by a field"""
    return sum([inst.value for inst in instructions if inst.direction == field])


def aim_tracker(instructions: list[Instruction]) -> int:
    aim, horizontal, depth = 0, 0, 0
    for instruction in instructions:
        if instruction.direction == Comand.forward:
            horizontal += instruction.value
            depth += aim * instruction.value
        elif instruction.direction == Comand.down:
            aim += instruction.value
        elif instruction.direction == Comand.up:
            aim -= instruction.value
    return horizontal * depth


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[Instruction]:
        instructions = []
        for d in data:
            direction, value = d.strip().split(" ")
            instructions.append(
                Instruction(direction=Comand(direction), value=int(value))
            )
        return instructions

    def part_one(self):
        forward = value_by_field(self.data, Comand.forward)
        up = value_by_field(self.data, Comand.up)
        down = value_by_field(self.data, Comand.down)
        return (down - up) * forward

    def part_two(self):
        return aim_tracker(self.data)
