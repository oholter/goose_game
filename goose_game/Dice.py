from random import randint
from goose_game.config import DICE_MIN, DICE_MAX


class Dice:
    @staticmethod
    def roll():
        return randint(DICE_MIN, DICE_MAX)
