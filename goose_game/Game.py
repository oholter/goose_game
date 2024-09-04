import logging
from goose_game.Dice import Dice
from goose_game.Space import Space
from goose_game.Board import Board
from goose_game.Player import Player

class Game:
    def __init__(self):
        self.players = []
        self.dice = Dice()
        self.board = Board()
        self.current_player = None
        self.is_finished = False

    def add_player(self):
        print("Add player: (min two players, press enter when you are finished)")
        name = input(">>> ")
        if name.strip():
            logging.debug("creating new player with name {}".format(name))
            new_player = Player(name, self.board)
            duplicate = False
            for player in self.players:
                if new_player.name.lower() == player.name.lower():
                    print("{} already existsting player".format(new_player.name))
                    duplicate = True

            if not duplicate:
                self.players.append(new_player)

            players = ""
            for p in self.players:
                players += p.name + ", "

            print("Players: {}".format(players))
            return new_player
        else:
            return False


    def get_next_player(self):
        if self.current_player is None:
            self.current_player = 0
        elif self.current_player < len(self.players)-1:
            self.current_player += 1
        else:
            self.current_player = 0

        return self.players[self.current_player]






