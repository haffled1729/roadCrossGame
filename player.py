"""
TO CREATE THE USER-CONTROLLED TURTLE OBJECT THAT CAN MOVE ALONG THE Y-AXIS DIRECTION.
TO RESET THE PLAYER BACK TO THE STARTING POSITION AFTER CROSSING THE FINISH LINE. 
CHECK IF THE PLAYER HAS COLLIDED WITH ANY CAR. 
"""

from turtle import Turtle
START = (0, -250)

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.left(90)
        self.start()

    def move(self):  # Move the turtle by 10 pixels
        self.forward(10)
    
    def start(self):   # Go back to the starting position defined by START
        self.goto(START)
    
    def collide(self, cars):       # Check if the turtle has collided with any car
        for c in cars:
            if self.distance(c) <= 25:
                return True