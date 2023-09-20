from turtle import Turtle, Screen
from random import randint
screen = Screen()
timmy = Turtle()
screen.colormode(255)
for i in range(3, 11):
    turn = 360/i
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    timmy.color(R, G, B)
    for _ in range(i):
        timmy.right(turn)
        timmy.forward(100)








screen.exitonclick()
