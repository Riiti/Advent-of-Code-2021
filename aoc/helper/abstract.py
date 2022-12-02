from typing import Protocol


class Challenge(Protocol):
    def __init__(self, data: list[str]) -> None:
        ...

    def preprocess(self, data: list[str]) -> list[str | int]:
        """Preprocess given data"""
        ...

    def part_one(self) -> int:
        """Solve part one of the quiz"""
        ...

    def part_two(self) -> int:
        """Solve part one of the quiz"""
        ...
