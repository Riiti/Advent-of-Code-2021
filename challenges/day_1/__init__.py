import numpy as np

from pathlib import Path

from challenges.helper.wrapper import day_wrapper


class Sonar:
    def __init__(self, array:np.array) -> None:
        self.values = array

    def get_num_of_larger(self)->int:
        return np.sum(np.where(self.values[:-1]<self.values[1:], 1, 0))

    def larger_in_window_of_three(self)->int:
        window_sum = self.values[:-2]+ self.values[1:-1] + self.values[2:]
        return np.sum(np.where(window_sum[:-1]<window_sum[1:], 1, 0))

    @classmethod
    def read_file(cls):
   
        path = f'{Path(__file__).parent}/data/sonar_values.txt'
        with open(path) as f:
            data = [int(line) for line in f.readlines()]
        return cls(np.array(data))
    
    @staticmethod
    @day_wrapper
    def run():
        sonar = Sonar.read_file()
        print(f"Values larger than the previous {sonar.get_num_of_larger()}.")
        print(f"Values larger than the previous in sliding window of three {sonar.larger_in_window_of_three()}.")


