import pandas as pd

from pathlib import Path

from challenges.helper.wrapper import day_wrapper


class Command:
    def __init__(self, frame:pd.DataFrame) -> None:
        self.values = frame

    def count_inst(self):
        sums = self.values.groupby('command').sum()
        return int((sums.loc['down']-sums.loc['up'])*sums.loc['forward'])

    def command_with_aim(self):
        pars = {'h_pos':0,
        'depth':0,
        'aim':0}
        for i, (command, amount) in self.values.iterrows():
            if command in ('up', 'down'):
                faktor = -1 if command == 'up' else +1
                pars['aim']+=amount*faktor
            elif command == 'forward':
                pars['h_pos']+=amount
                pars['depth']+=pars['aim']*amount
            else:
                raise ValueError('Unknown command: '+ command)
        return pars['h_pos']*pars['depth']

    @classmethod
    def read_file(cls):
        path = f'{Path(__file__).parent}/data/commands.txt'
        return cls(pd.read_csv(path, sep=' ', names=['command', 'amount']))

    @staticmethod
    @day_wrapper
    def run():
        com = Command.read_file()
        print(f"Submarine at {com.count_inst()}.")
        print(f"Submarine with aim at {com.command_with_aim()}.")

