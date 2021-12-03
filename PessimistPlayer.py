from Player import *

class Pessimist(Player):
    def __init__(self, name):
        Player.__init__(self,name)
        self.type = "Pessimist"

    def choosePath(self, board):
        # The pessimist player will only go for the star if they currently have enough coins
        if self.coins >= 20 :
            return board.shortestPath()
        else:
            return board.secondShortestPath()
