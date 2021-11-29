import random
from random import shuffle
from Space import *

STAR_SPACES = [3,6,9,12,15,18]
NEIGHBORS = [1,2,3,4,[5,20],6,7,8,9,10,11,12,13,14,15,16,17,18,19,0,21,22,23,6]

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
            print(f"{self.spaces[x].debugTellSecrets()}")

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
        current = player.current_space
        for x in range(0, roll):
            go_to = self.spaces[current].next_space
            if type([go_to]) == type([0]):
                player.choosePath(self)
            if go_to == self.current_star_space:
                if player.buyStar():
                    self.current_star_space = self.setCurrentStarSpace()
                go_to = go_to.next_space
        player.current_space = go_to

    # def movePlayer(self, player, roll):
    #     go_to = player.current_space
    #     for x in range(0, roll):
    #         go_to = self.nextSpace(go_to)
    #         if go_to == self.current_star_space:
    #             if player.buyStar():
    #                 self.current_star_space = self.setCurrentStarSpace()
    #             go_to = self.nextSpace(go_to)
    #     player.current_space = go_to
