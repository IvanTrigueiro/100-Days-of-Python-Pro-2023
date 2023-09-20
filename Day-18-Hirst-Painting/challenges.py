from turtle import Turtle, Screen
from random import randint, choice
screen = Screen()
timmy = Turtle()
screen.colormode(255)


def random_color():
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    return R, G, B


# # Turtle Challenge loop shapes with same sized sides
def loop_shapes():
    for i in range(3, 11):
        turn = 360/i
        timmy.color(random_color())
        for _ in range(i):
            timmy.right(turn)
            timmy.forward(100)


# # Turtle Challenge Random Walk
def random_walk(angles_list):
    direction = choice(angles_list)
    timmy.setheading(direction)
    timmy.forward(20)


def walk():
    angles = [0, 90, 180, 270]
    timmy.speed(8)
    timmy.width(6)
    for _ in range(200):
        timmy.color(random_color())
        random_walk(angles)


# # Turtle Challenge Draw Spirograph
def spirograph():
    timmy.speed("fastest")
    degrees = 5
    for _ in range(int(360/degrees)):
        timmy.circle(100)
        timmy.left(degrees)
        timmy.color(random_color())


# loop_shapes()
# walk()
spirograph()

screen.exitonclick()
