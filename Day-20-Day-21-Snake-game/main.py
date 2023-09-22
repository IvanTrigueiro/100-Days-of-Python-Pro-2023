from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
initial_positions = [(0, 0), (-20, 0), (-40, 0)]
for turtle_index in range(0, 3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(initial_positions[turtle_index])

screen.exitonclick()