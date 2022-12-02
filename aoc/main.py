from pathlib import Path

from helper.filereader import read_file
from aoc.challenges.year_2022.day_2 import Solver

day = "2"
year = "2022"

data_path = (
    Path(__file__).parent / f"challenges/year_{year}/day_{day}/data/data.txt"
)
data = read_file(data_path)
solver = Solver(data)
print(solver.part_two())
