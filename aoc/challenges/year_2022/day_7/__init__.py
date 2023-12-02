from collections import defaultdict
from aoc.helper.abstract import Challenge

DISK_SPACE = 70000000
NEEDED = 30000000


def parse_directory(data: list[str]) -> dict[str, int]:
    filesystem = defaultdict(int)
    folder = []
    for inst in data:
        match inst.split():
            case "$", "cd", "/":
                folder = ["/"]
            case "$", "cd", "..":
                folder.pop()
            case "$", "cd", x:
                folder.append(x)
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case size, _:
                filesystem = update_filesizes(filesystem, folder, size)
    return filesystem


def update_filesizes(
    filesystem: dict[str, int], folder: list[str], size: str
) -> dict[str, int]:
    base = ""
    for el in folder:
        base = base + el
        filesystem[base] += int(size)
    return filesystem


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[str]:
        return [d.strip() for d in data]

    def part_one(self) -> int:
        filesystem = parse_directory(self.data)
        return sum([file for file in filesystem.values() if file < 100_000])

    def part_two(self) -> int:
        filesystem = parse_directory(self.data)
        missing_space = NEEDED - (DISK_SPACE - max(filesystem.values()))
        return min(
            [file for file in filesystem.values() if file > missing_space]
        )
