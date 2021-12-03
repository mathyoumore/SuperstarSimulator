import random
from random import shuffle
from Space import *

STAR_SPACES = [3,6,9,12,15,18]
NEIGHBORS = [1,2,3,4,[5,20],6,7,8,9,10,11,12,13,14,15,16,17,18,19,0,21,22,23,14]
SHORTEST_TO_STAR = {
    3: 20,
    6: 5,
    9: 5,
    12: 5,
    15: 20,
    18: 20
}
SECOND_TO_STAR = {
    3: 5,
    6: 20,
    9: 20,
    12: 20,
    15: 5,
    18: 5
}

class Board:
    def __init__(self, name):
        self.name = name
        self.spaces = []
        self.colors = ["BLUE", "RED", "GREEN"]
        self.current_star_space = -1
        self.star_spaces = []
        self.initSpaces()
        self.resetStarSpaces()
        self.current_star_space = self.setCurrentStarSpace()

    def initSpaces(self):
        space = ""
        for x in range(0, len(NEIGHBORS)):
            seed = random.randint(0, 99)
            if seed < 64:
                space = "BLUE"
            elif seed < 77:
                space = "RED"
            else:
                space = "GREEN"
            self.spaces.append(Space(space, x, NEIGHBORS[x]))

    def resetStarSpaces(self):
        for s in STAR_SPACES:
            self.star_spaces.append(s)

    def setCurrentStarSpace(self):
        s = random.randrange(len(self.star_spaces))
        while s == self.current_star_space:
            s = random.randrange(len(self.star_spaces))
        self.star_spaces[s], self.star_spaces[-1] = self.star_spaces[-1], self.star_spaces[s]
        new_star_space = self.star_spaces.pop()
        if len(self.star_spaces) == 0:
            self.resetStarSpaces()
        print(f"Hi, I moved the star to {new_star_space}")
        return new_star_space

    def debugTellSecrets(self):
        for x in self.spaces:
            print("{0} at {1}".format(x.color, x.address))

    def nextSpace(self, address):
        match self.spaces[address].address:
            case 19:
                return 0
            case _:
                return address + 1

    def colorAt(self, space_address):
        return self.spaces[space_address].color

    def movePlayer(self, player, roll):

        # Go one-by-one and check each space for a special event
        for x in range(0, roll):

            # look at the next space
            go_to = self.spaces[player.current_space].next_space

            # if the next space is a junction, logic depends on player intelligence
            if type(go_to) == type([0]):
                    go_to = player.choosePath(self)
                    
            # if the next space is a star
            if go_to == self.current_star_space:
                if player.buyStar():
                    self.current_star_space = self.setCurrentStarSpace()
                # stars aren't a space, so move to the next one
                go_to = self.nextSpace(go_to)

            # move player to the next space they need to go to, store that new space

            player.current_space = go_to
            player.visited.append(go_to)

    def shortestPath(self):
        return SHORTEST_TO_STAR[self.current_star_space]

    def secondShortestPath(self):
        return SECOND_TO_STAR[self.current_star_space]

    def debugJunction(self):
        return 5
