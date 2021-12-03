from Game import *

g1 = Game(die_size = 10, turn_limit = 20)
g2 = Game(die_size = 6, turn_limit = 20)
for x in range(2):
    g1.playGame()
    g2.playGame()

# TODO

"""

* Will need to run a distance-to-star based on every star position and board position
*   Above sounds terrible to do by hand, so we'll need a tool to do that for us instead of us doing it.

* Planning greedy - Avoid is a player is closer, otherwise goes for it
* Planning pessimist - Only go if no other players are closer and if they have enough coins
* Planning pragmatist - Only go if no toher players are closer and either they have enough coins or will land on blue to put the at 20+
* Perfect pessimist - If there are closer players, only go if they don't have enough coins. Even then (or otherwise), only go if enough coins or will land on blue to go over 20
* Ignoration - Abandon brain, follow RNGod
* Human - Score likelihood of getting a star based on all players' positions, stars, and roll, then use that score to decide likelihood that they do some unpredictable nonsense instead
* CSV output
"""
