from world import World
from animal import Zebra, Lion 


world = World(width=50, height=50)

world.initialize(create_zebra=Zebra, create_lion=Lion)

year = 0 
while True: 
    print (f"Year: {year}")
    input() 
    world.display()
    world.update()
    year+= 1 

