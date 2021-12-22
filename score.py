"""
TO WRITE THE CURRENT LEVEL
DRAW THE FINISH LINE
TO UPDATE THE LEVEL COUNT
DISPLAY GAMEOVER SEQUENCE
"""

from turtle import Turtle
FONT = ("Courier", 12, "bold")
GO_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.difficulty = 1
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.score()
        
    
    def score(self, l = 0):   # Update score and write the same on the screen along with the finish line
        if l:
            self.level += 1
        self.difficulty *= 0.8
        self.clear()
        self.goto(-270, 250)
        self.pendown()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.penup()
        self.goto(-300, 240)
        self.pendown()
        self.forward(600)
        self.penup()
        self.home()

    def gameover(self):    # To write GAME OVER on screen
        self.pendown()
        self.write("GAME OVER", align="center", font=GO_FONT)