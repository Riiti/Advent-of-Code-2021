from dataclasses import dataclass
from aoc.helper.abstract import Challenge

from itertools import product


@dataclass
class Grid:
    rows: list[list[int]]
    columns: list[list[int]]


@dataclass
class Tree:
    height: int
    x: int
    y: int


def collect_basedata(
    data: list[list[int]],
) -> tuple[Grid, list[tuple[int, int]]]:
    width = len(data)
    height = len(data[0])
    nums = product(range(1, width - 1), range(1, height - 1))
    columns = list(map(list, zip(*data)))
    grid = Grid(rows=data, columns=columns)
    return grid, list(nums)


def biggest_tree(data: list[list[int]]) -> int:
    grid, nums = collect_basedata(data)
    visible = sum(
        [check_for_visibility(grid, Tree(data[x][y], x, y)) for x, y in nums]
    )
    return visible


def check_for_visibility(grid: Grid, tree: Tree) -> bool:
    row_maxes = split_list_at_index(grid.rows[tree.x], tree.y)
    column_maxes = split_list_at_index(grid.columns[tree.y], tree.x)
    return tree.height > min([*row_maxes, *column_maxes])


def split_list_at_index(data: list[int], index: int) -> tuple[int, int]:
    return max(data[:index]), max(data[index + 1 :])


def scenic_score(data: list[list[int]]) -> int:
    grid, nums = collect_basedata(data)
    return max(
        [viewing_distance(grid, Tree(data[x][y], x, y)) for x, y in nums]
    )


def viewing_distance(grid: Grid, tree: Tree) -> int:
    row = grid.rows[tree.x]
    column = grid.columns[tree.y]
    left = calc_distance(row[: tree.y], tree.height, True)
    right = calc_distance(row[tree.y + 1 :], tree.height, False)
    up = calc_distance(column[: tree.x], tree.height, True)
    down = calc_distance(column[tree.x + 1 :], tree.height, False)
    return left * right * up * down


def calc_distance(elements: list[int], height: int, reverse: bool) -> int:
    if reverse:
        elements = elements[::-1]
    count = 0
    for el in elements:
        count += 1
        if el >= height:
            break
    return count


class Solver(Challenge):
    def __init__(self, data: list[str]) -> None:
        self.data = self.preprocess(data)

    def preprocess(self, data: list[str]) -> list[list[int]]:
        return [[int(num) for num in d.strip()] for d in data]

    def part_one(self) -> int:
        width = len(self.data)
        height = len(self.data[0])
        surrounding = 2 * (width + height - 2)
        return biggest_tree(self.data) + surrounding

    def part_two(self) -> int:
        return scenic_score(self.data)
