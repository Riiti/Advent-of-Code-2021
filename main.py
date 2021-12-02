from challenges.day_1 import Sonar

print(f'{"*"*30} Day 1 {"*"*30}')
sonar = Sonar.read_file()
print(f"Values larger than the previous {sonar.get_num_of_larger()}.")
print(f"Values larger than the previous in sliding window of three {sonar.larger_in_window_of_three()}.")
print(f'{"*"*30} Day 1 {"*"*30}')