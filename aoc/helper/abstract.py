from abc import ABC, abstractmethod


class Challenge(ABC):
    @abstractmethod
    def __init__(self, data) -> None:
        """Stores the Data from a file in a variable"""

    @abstractmethod
    def part_one(self) -> None:
        """Solve part one of the quiz"""

    @abstractmethod
    def part_two(self) -> None:
        """Solve part one of the quiz"""

    @classmethod
    @abstractmethod
    def read_file(cls):
        """Read data from given file"""

    @staticmethod
    @abstractmethod
    def run():
        """Solve the quiz"""
