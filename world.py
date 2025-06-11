import random

class World:
    def __init__(self, width: int = 50, height: int = 50):
        self.width = width
        self.height = height
        self.animals = []  # list of animals

    def initialize(self, create_zebra, create_lion):
        # make a list of all positions
        positions = []
        for x in range(self.width):
            for y in range(self.height):
                positions.append((x, y))

        random.shuffle(positions)

        # place 20 zebras
        for _ in range(20):
            x, y = positions.pop()
            self.animals.append(create_zebra(x, y))

        # place 5 lions
        for _ in range(5):
            x, y = positions.pop()
            self.animals.append(create_lion(x, y))

    def display(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                symbol = "."
                for a in self.animals:
                    if a.x == x and a.y == y:
                        if a.species == "zebra":
                            symbol = "0"
                        elif a.species == "lion":
                            symbol = "X"
                        break
                row += symbol
            print(row)