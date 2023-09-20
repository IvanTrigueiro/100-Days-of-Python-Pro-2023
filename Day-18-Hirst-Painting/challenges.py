from turtle import Turtle, Screen
from random import randint, choice
screen = Screen()
timmy = Turtle()
screen.colormode(255)

# # Turtle Challenge loop shapes with same sized sides
# for i in range(3, 11):
#     turn = 360/i
#     R = randint(0, 255)
#     G = randint(0, 255)
#     B = randint(0, 255)
#     timmy.color(R, G, B)
#     for _ in range(i):
#         timmy.right(turn)
#         timmy.forward(100)


# # Turtle Challenge Random Walk
def random_walk(angles_list):
    direction = choice(angles_list)
    timmy.setheading(direction)
    timmy.forward(20)


angles = [0, 90, 180, 270]
timmy.speed(8)
timmy.width(6)
for _ in range(200):
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    timmy.color(R, G, B)
    random_walk(angles)























screen.exitonclick()
