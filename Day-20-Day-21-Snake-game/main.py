from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "W")
screen.onkey(snake.down, "S")
screen.onkey(snake.left, "A")
screen.onkey(snake.right, "D")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 13:
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.xcor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
