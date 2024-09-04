import logging
from goose_game.Dice import Dice
from goose_game.config import (
    BOARD_SIZE, BRIDGE_END, END_SPACE_IDX, DICE_MIN, DICE_MAX
)


class Player:
    def __init__(self, name, board):
        self.name = name
        self.current_space = board.start_space
        self.last_throw = None
        self.board = board
        self.has_finished = False

    def move(self, rolls):
        dice_roll = rolls[0] + rolls[1]
        new_space_idx = self.current_space.idx + dice_roll
        logging.debug("current_space: {}".format(self.current_space))
        if new_space_idx < BOARD_SIZE:
            new_space = self.board.get_space(new_space_idx)
            logging.debug("new_space: {}".format(new_space))
            print("{} rolls {},{}. {} moves from {} to {}".
                  format(self.name, rolls[0], rolls[1], self.name, self.current_space.idx, new_space.idx))
        else:
            logging.debug("bouncing...")
            new_space = self.board.get_space(END_SPACE_IDX)
            logging.debug("new_space: {}".format(new_space))
            rest = (dice_roll + self.current_space.idx) - END_SPACE_IDX
            new_idx = END_SPACE_IDX - rest
            print("{} rolls {},{}. {} moves from {} to {}. {} bounces. {} returns to {}".
                  format(self.name, rolls[0], rolls[1], self.name, self.current_space.idx, new_space.idx, self.name, self.name, new_idx))
            new_space = self.board.get_space(new_idx)
            logging.debug("new_space: {}".format(new_space))

        return new_space



    def play(self):
        valid_input = False
        while not valid_input:
            print("{} rolls:".format(self.name))
            roll = input(">>> ")
            if roll:
                # todo: handle errors
                try:
                    rolls = roll.split(",")
                    logging.debug("rolls: {}".format(rolls))
                    roll1, roll2 = roll.split(",")
                    rolls = [0]*2
                    rolls[0] = int(roll1)
                    rolls[1] = int(roll2)
                    logging.debug("rolls[0]: {}".format(rolls[0]))
                    logging.debug("rolls[1]: {}".format(rolls[1]))
                    if rolls[0] > DICE_MAX:
                        print("Value {} too high".format(rolls[0]))
                    elif rolls[0] < DICE_MIN:
                        print("Value {} too low".format(rolls[0]))
                    elif rolls[1] > DICE_MAX:
                        print("Value {} too high".format(rolls[1]))
                    elif rolls[1] < DICE_MIN:
                        print("Value {} too low".format(rolls[1]))
                    else:
                        valid_input = True
                except ValueError:
                    print("Invalid input \"{}\": The string should be two digits with a comma (e.g., \"1,2\" or \"5,6\")".format(roll))
            else:
                rolls = [0]*2
                rolls[0] = Dice.roll()
                rolls[1] = Dice.roll()
                logging.debug("rolls[0]: {}".format(rolls[0]))
                logging.debug("rolls[1]: {}".format(rolls[1]))
                valid_input = True

        while True:
            # Case 1: Player wins
            # Case 2: Player goes passed Finish
            # Case 3: Player hits goose
            # Case 5: Player hits bridge

            next_space = self.move(rolls)

            # Case Player hits other player's space
            if next_space.player is not None:
                logging.debug("moving {} back to {}".format(next_space.player, next_space))
                # player B is moved to player A's current space
                playerb = next_space.player
                print("On {} there is {}, who returns to {}".
                      format(next_space.idx, playerb.name, self.current_space.idx))
                playerb.current_space = self.current_space
                self.current_space.player = playerb
                next_space.player = None

            if next_space.is_finish:
                self.has_finished = True
                self.current_space.player = None
                self.current_space = next_space
                self.current_space.player = self
                break
            elif next_space.is_goose:
                print("The Goose. {} moves again.".format(self.name))
                self.current_space.player = None
                self.current_space = next_space
                self.current_space.player = self
            elif next_space.is_bridge:
                next_space = self.board.get_space(BRIDGE_END)
                print("The bridge. {} moves to {}".format(self.name, next_space.idx))
                self.current_space.player = None
                self.current_space = next_space
                self.current_space.player = self
                break
            else:  # normal move
                self.current_space.player = None
                self.current_space = next_space
                self.current_space.player = self
                break


    def __str__(self):
        return "Player: {}".format(self.name)
