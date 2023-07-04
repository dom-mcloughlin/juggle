import unittest

import pandas

from src.constants import *
from src.exceptions import BallDroppedError
from src.state import Action, Game

pandas.set_option('display.max_rows', None)


class TestActions(unittest.TestCase):
    def test_1(self):
        action_df = pandas.read_csv('data/actions.csv')
        actions = action_df.apply(lambda x: Action(*x), axis=1)
        print("\n", actions[0])
        game = Game()
        game.steps(actions)
        df = game.get_history()
        game.write_history()
        print(df)

    def test_2(self):
        action_df = pandas.read_csv('data/actions.csv')
        actions = action_df.apply(lambda x: Action(*x), axis=1)
        print(actions)
        game = Game()
        try:
            game.steps(actions)
        except:
            BallDroppedError
        game.write_history()
        game.plot_history()
        return
