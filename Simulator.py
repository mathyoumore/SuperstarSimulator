from Game import *

g1 = Game(die_size = 10, turn_limit = 20)
g2 = Game(die_size = 6, turn_limit = 20)
for x in range(10):
    g1.playGame()
    g2.playGame()

# TODO
"""
* Branching path logic - case switch that has every star position memorized 
* Greedy player
* Pessimist player
* Planning greedy
* Planning pessimist
* Human
* CSV output
"""
