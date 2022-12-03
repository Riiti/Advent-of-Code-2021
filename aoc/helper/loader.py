import os
from pathlib import Path
from types import ModuleType

from helper.filereader import read_file
from importlib.machinery import SourceFileLoader
import argparse


def generate_base_path(day: str, year: str) -> Path:
    return Path(__file__).parents[1] / f"challenges/year_{year}/day_{day}"


def load_solver(base_path: Path) -> ModuleType:
    module_path = base_path / "__init__.py"
    try:
        return SourceFileLoader("solver", str(module_path)).load_module()
    except FileNotFoundError:
        create_if_doesnt_exist(base_path)


def create_if_doesnt_exist(base_path: Path) -> None:
    create = input(
        "The challenge you are looking for does not exist want to create it now y/n?"
    )
    if create.strip() == "y":
        create_files(base_path)
        raise AssertionError("Files createt, you can start on the solution now")
    raise FileNotFoundError("No solution for the quiz you requestet")


def create_files(base_path: Path) -> None:
    os.makedirs(base_path / "data")
    Path(base_path / "__init__.py").touch()
    Path(base_path / "data/data.txt").touch()


def load_data(base_path: Path) -> list[str]:
    data_path = base_path / "data/data.txt"
    return read_file(data_path)


def solve_quiz(day: str, year: str) -> None:
    path = generate_base_path(day, year)
    module = load_solver(path)
    data = load_data(path)
    solver = module.Solver(data)
    print(solver.part_one())
    print(solver.part_two())


def collect_arguments() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "day", help="Enter the day of the challenge you want to solve", type=int
    )
    parser.add_argument(
        "year",
        help="Enter the year of the challenge you want to solve",
        type=int,
    )
    args = parser.parse_args()
    solve_quiz(args.day, args.year)
