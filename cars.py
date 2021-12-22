"""
TO CREATE CARS, PLACE THEM AT RANDOM POSITIONS OUTSIDE THE PLAYSCREEN, MOVE THEM AND RE-PLACE THEM TO A DIFFERENT POSITION
AFTER THEY MOVE OUTSIDE THE PLAYSCREEN AREA
"""

from turtle import Turtle
from random import choice, randrange
NO_OF_CARS = 30
COLORS = ["red", "blue", "yellow", "gray", "pink", "purple", "cyan", "magenta"]

class Cars(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.queue = []             # Stores all the turtle objects that emulate cars in this game
        self.flow = 0
        for i in range(NO_OF_CARS):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.setheading(180)
            car.color(choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)     # Length of the car is 40 pixels and width is 20 pixels
            car.goto(self.rand_pos())                       # Place the car at a random x, y position
            self.queue.append(car)                          # Add the car to the list of cars

    def rand_pos(self):         # To generate random coordinates for the cars
            x = randrange(350, 1000, 100)
            y = randrange(-200, 200, 70)
            return (x,y)

    def pos_reset(self):        # To reset the cars to the rightside to enable reusing of existing turtle objects
        for i in range(NO_OF_CARS):    
            if self.queue[i].xcor() < -350:
                self.queue[i].goto(self.rand_pos())

    def move_jam(self):         # To move all the cars by 20 pixels, when called before every screen update
        for i in self.queue:    
            i.forward(20)