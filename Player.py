from Board import *


class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.stars = 0
        self.current_space = 0
        self.wins = 0
        self.visited = []
        self.type = "UNASSIGNED PLAYER"

    def buyStar(self):
        if self.coins >= 20:
            self.coins -= 20
            self.stars += 1
            return True
        return False

    def addCoins(self, coins_to_add):
        self.coins += coins_to_add

    def winMiniGame(self):
        self.wins += 1

    def status(self):
        return f"{self.name} ({self.type}) at {self.current_space}: {self.coins}c, {self.stars}s "

    def choosePath(self, board):
        print("UNASSIGNED PLAYER PASSING JUNCTION!!!")
        return board.debugJunction()
