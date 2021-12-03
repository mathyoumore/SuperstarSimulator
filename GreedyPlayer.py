from Player import *

class Greedy(Player):
    def __init__(self, name):
        Player.__init__(self,name)
        self.type = "Greedy"

    def choosePath(self, board):
        # The greedy player will always go to the star, whether or not they have enough coins
        return board.shortestPath()
