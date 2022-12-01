from typing import Protocol


class Challenge(Protocol):
    def __init__(self) -> None:
        ...

    def part_one(self) -> None:
        """Solve part one of the quiz"""
        ...

    def part_two(self) -> None:
        """Solve part one of the quiz"""
        ...

    def read_file():
        """Solve the quiz"""
        ...
