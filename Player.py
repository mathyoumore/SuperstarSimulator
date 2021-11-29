class Player:
    def __init__ (self, name):
        self.name = name
        self.coins = 0
        self.stars = 0
        self.current_space = 0
        self.wins = 0

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
        return f"{self.name}: {self.coins}c, {self.stars}s "

    def choosePath(self, board):
        # Run down each path, count spaces until star
        """

        This works, but freaks out because loops in lists are hard.
        Easier to build a case switch for the shortest star path for every junction
        
        spaces = [0,1,2,3,4,5,6,7,8,9,10]
        neighbors = [1,2,3,[4,7],5,6,0,[8,9],10,0]
        star = 9
        current_position = 3

        potential_paths = neighbors[current_position]
        distances_to_star = []
        distance = 0
        shortest_path = [float("inf"),-1]

        #def foo (potential_paths):
        for index, p in enumerate(potential_paths):
            still_looking = True
            distance = 0
            looking_space = p
            while still_looking:
                if neighbors[looking_space] == star or neighbors[looking_space] == current_position:
                    still_looking = False
                distance += 1
                looking_space = neighbors[looking_space]

            if distance < shortest_path[0]:
                shortest_path[0] = p
                shortest_path[1] = distance

        print(f"The shortest path is via {shortest_path[0]} at {shortest_path[1]} spaces.")
        """
