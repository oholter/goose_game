import logging
from goose_game.Game import Game

from goose_game.config import (
    BOARD_SIZE, START_SPACE_IDX, END_SPACE_IDX, BRIDGE_IDX, BRIDGE_END, GOOSE_IDXS
)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        #level=logging.DEBUG,
        format="%(asctime)s : %(levelname)s : %(message)s"
    )

    logging.debug("Creating goose game")
    logging.debug("Board size: {}".format(BOARD_SIZE))
    logging.debug("Start_space_idx: {}".format(START_SPACE_IDX))
    logging.debug("End_space_dx: {}".format(END_SPACE_IDX))
    logging.debug("Bridge_idx: {}".format(BRIDGE_IDX))
    logging.debug("Bridge_end: {}".format(BRIDGE_END))
    logging.debug("Goose_idxs: {}".format(GOOSE_IDXS))

    game = Game()

    while True:
        new_player = game.add_player()
        if not new_player:
            break

    if len(game.players) < 2:
        print("Game is for at least two players. Quitting...")
        exit()


    while not game.is_finished:
        current_player = game.get_next_player()
        current_player.play()
        if current_player.has_finished:
            game.is_finished = True
            print("{} wins!!".format(current_player.name))
