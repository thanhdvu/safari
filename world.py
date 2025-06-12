import random

class World:
    def __init__(self, width: int = 50, height: int = 50):
        """
        지도의 크기를 설정하고, 동물 리스트를 초기화합니다.
        """
        self.width = width
        self.height = height
        self.animals = []  # list of animals

    def initialize(self, create_zebra, create_lion):
        """
        얼룩말 20마리, 사자 5마리를 무작위 위치에 배치합니다.
        """
        positions = []
        for x in range(self.width):
            for y in range(self.height):
                positions.append((x, y))

        random.shuffle(positions)

        for _ in range(20):
            x, y = positions.pop()
            self.animals.append(create_zebra(x, y))

        for _ in range(5):
            x, y = positions.pop()
            self.animals.append(create_lion(x, y))

    def display(self):
        """
        . = 빈칸, 0 = 얼룩말, X = 사자
        """
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                symbol = "."
                for a in self.animals:
                    if a.x == x and a.y == y:
                        if a.species == "zebra":
                            symbol = a.symbol
                        elif a.species == "lion":
                            symbol = a.symbol
                        break
                row += symbol
            print(row)
            
    def update(self):
        for a in self.animals:
            a.move(self.width, self.height)
        
        for a in list(self.animals): 
            a.act(self.animals, self.width, self.height) 
