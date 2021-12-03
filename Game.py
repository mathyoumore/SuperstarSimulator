from Board import *
from Player import *
from GreedyPlayer import *
from PessimistPlayer import *


class Game:
    def __init__(self, die_size, turn_limit):
        self.board = Board('Fixed Star')
        self.die_size = die_size
        self.turn_limit = turn_limit
        self.reset()

    def reset(self):
        self.initPlayers()
        self.initMeasures()
        self.board = Board('Fixed Star')

    def initPlayers(self):
        self.players = [
            Greedy("Mario"),
            Player("Wario"),
            Pessimist("Luigi"),
            Player("Waluigi")
        ]

    def initMeasures(self):
        self.one_v_three = 0
        self.two_v_two = 0
        self.free_for_all = 0
        self.current_turn = 0

    def roll(self):
        return random.randrange(1, self.die_size)

    def playGame(self):
        while self.current_turn < self.turn_limit:
            print (f"-------------------------- Turn {self.current_turn} -----------------------------------")
            self.playTurn()
            self.current_turn += 1

        print("Game over")
        for p in self.players:
            print(p.status())
            print(f"{p.visited}")
        self.results()
        self.reset()

    def playTurn(self):
        for p in self.players:
            print (f"-------------------------- Player {p.name} ----------------------")
            self.board.movePlayer(p, self.roll())
        self.minigame()

    def minigame(self):
        # Determine teams
        reds = []
        blues = []
        for p in self.players:
            color = self.board.colorAt(p.current_space)
            match color:
                case 'GREEN':
                    if random.randint(0, 1) == 1:
                        reds.append(p)
                    else:
                        blues.append(p)
                case 'RED':
                    reds.append(p)
                case 'BLUE':
                    blues.append(p)
                case _:
                    raise ValueError(
                        f"Unexpected color, {color}, for player {p.name}")

        # Record game
        match len(blues):
            case 0:
                self.free_for_all += 1
            case 1:
                self.one_v_three += 1
            case 2:
                self.two_v_two += 1
            case 3:
                self.one_v_three += 1
            case 4:
                self.free_for_all += 1
            case _:
                raise ValueError(
                    f"Something has gone wrong. Blues has {len(blues)} players")

        # Pick winner, award coins
        winners = []
        if blues == 4:
            winners = blues[random.randint(0, len(blues) - 1)]
        elif blues == 0:
            winners = reds[random.randint(0, len(reds) - 1)]
        else:
            if random.randint(0, 1) == 0:
                winners = blues
            else:
                winners = reds

        for w in winners:
            w.winMiniGame()
            w.addCoins(10)

    def results(self):
        print(f"d{self.die_size}")
        print(
            f"4v4: {self.free_for_all}\n2v2: {self.two_v_two}\n1v3: {self.one_v_three}")
        print(
            f"""{self.players[0].status()}\n{self.players[1].status()}\n{self.players[2].status()}\n{self.players[3].status()}""")
        print("----------------------")
