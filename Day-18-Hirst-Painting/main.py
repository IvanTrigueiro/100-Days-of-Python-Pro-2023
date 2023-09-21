# import colorgram
# number_of_colors = 30
# colors_rgb = []
# colors_extracted = colorgram.extract('image.jpg', number_of_colors)
# for i in range(number_of_colors):
#     R = colors_extracted[i].rgb.r
#     G = colors_extracted[i].rgb.g
#     B = colors_extracted[i].rgb.b
#     colors_rgb.append((R, G, B))
# print(colors_rgb)


from turtle import Turtle, Screen
from random import choice


# Setting timmy starting position and starting values
timmy = Turtle()
timmy.penup()
timmy.hideturtle()
timmy_position_x = -250
timmy_position_y = -250
timmy.setposition(timmy_position_x, timmy_position_y)
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)
color_list = [(238, 246, 243), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]
paint_size = 10

for _ in range(paint_size):
    for _ in range(paint_size):
        timmy.dot(20, choice(color_list))
        timmy.forward(50)
    timmy_position_y += 50
    timmy.setposition(-250, timmy_position_y)
timmy.hideturtle()

screen.exitonclick()
