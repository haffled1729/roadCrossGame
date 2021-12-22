"""
THE MAIN GAMEPLAY INTERFACE THAT USER INTERACTS WITH.
CREATE THE PLAYER, SCOREBOARD AND THE CARS. 
UPDATE THE SCREEN PERIODICALLY TO PRODUCE ACTIONS. 
"""

from turtle import Screen
from player import Player
from score import Scoreboard
from cars import Cars
from time import sleep

scr = Screen()
scr.setup(width = 600, height = 600)
scr.tracer(0)

turt = Player()
scr.update()
cars = Cars()
score = Scoreboard()

game_on = True

scr.listen()
while game_on:
    sleep(0.05 * score.difficulty)
    scr.update()
    scr.onkey(key="Up", fun=turt.move)   # Move the turtle by 10 pixels when up key is pressed
    if cars.flow == 0:
        cars.move_jam()
        cars.flow = 3
    cars.pos_reset()
    if turt.ycor() == 240:   # Check if the turtle has touched the finish line
        turt.start()
        score.score(1)
    elif turt.collide(cars.queue):    # Check if the turtle has collided with any car
        score.gameover()
        game_on = False
    cars.flow -= 1
scr.exitonclick()
