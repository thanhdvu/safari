import random 

class Animal:
    def __init__(self, x: int, y: int, species: str, symbol: str):
        self.x = x
        self.y = y
        self.species = species
        self.symbol = symbol

    def move(self, width, height):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        new_x = self.x + dx
        new_y = self.y + dy

        if 0 <= new_x < width: 
            self.x = new_x
        if 0 <= new_y < height: 
            self.y = new_y 

    def act(self, others:list):
        pass
        


class Zebra(Animal):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "zebra", "0")
        self.age = 0 
    
    def act(self, others:list, width: int, height: int): 
        self.age += 1

        if self.age >= 3: 
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions) 

            occupied = {(a.x, a.y) for a in others}
            for dx, dy in directions:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    #번식 
                    if (nx, ny) not in occupied:
                        others.append(Zebra(nx, ny))
                        self.age = 0
                        break



class Lion(Animal):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "lion", "X")
        self.age = 0 
        self.hungry_years = 0 

    def act(self, others: list, width: int, height:int): 
        self.age += 1
        prey = None
        for a in others: 
            if a.species =="zebra":
                if max(abs(self.x - a.x), abs(self.y - a.y)) == 1: 
                    prey = a
                    break 
        
        if prey: 
            others.remove(prey)
            self.hungry_years = 0 
        else: 
            self.hungry_years += 1

        #5년 굶으면 사망 
        if self.hungry_years >= 5:
            others.remove(self)
            return 
        
        #번식 (5살 이상) )
        if self.age >= 5: 
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions) 

            occupied = {(a.x, a.y) for a in others}
            for dx, dy in directions:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    #번식 
                    if (nx, ny) not in occupied:
                        others.append(Lion(nx, ny))
                        self.age = 0
                        break

