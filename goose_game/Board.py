import logging
from goose_game.Space import Space
from goose_game.config import (
    BOARD_SIZE, START_SPACE_IDX, END_SPACE_IDX
)


class Board:
    def __init__(self):
        self.space = [None] * BOARD_SIZE

        for i in range(START_SPACE_IDX, END_SPACE_IDX+1):
            logging.debug("creating space {}".format(i))
            self.space[i] = Space(i)

        self.start_space = self.space[START_SPACE_IDX]
        self.end_space = self.space[END_SPACE_IDX]

    def get_space(self, idx):
        return self.space[idx]
