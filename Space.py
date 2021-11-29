class Space:
    def __init__ (self, color, address, next_space):
        self.color = color
        self.address = address
        self.next_space = next_space

    def debugTellSecrets(self):
        return f"{self.color} at {self.address} with next space {self.next_space}"
