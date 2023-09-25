import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
screen.onkeypress(player.move_up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    scoreboard.display_score()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            car_manager.reset_speed()
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.start_position()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
