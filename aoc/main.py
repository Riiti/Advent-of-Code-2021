from pathlib import Path

from helper.filereader import read_file
from aoc.challenges.year_2021.day_3 import Solver

day = "3"
year = "2021"

data_path = (
    Path(__file__).parent / f"challenges/year_{year}/day_{day}/data/data.txt"
)
data = read_file(data_path)
solver = Solver(data)
print(solver.part_one())
