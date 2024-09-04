from goose_game.config import (
    START_SPACE_IDX, END_SPACE_IDX, BRIDGE_IDX, GOOSE_IDXS
)


class Space:
    def __init__(self, idx):
        self.idx = idx
        self.is_start = True if idx == START_SPACE_IDX else False
        self.is_goose = True if idx in GOOSE_IDXS else False
        self.is_bridge = True if idx == BRIDGE_IDX else False
        self.is_finish = True if idx == END_SPACE_IDX else False
        self.player = None

    def __str__(self):
        return "Space: {}".format(self.idx)
