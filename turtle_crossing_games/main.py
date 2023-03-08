from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()


def move_up():
    player.forward(20)


screen.onkey(move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    scoreboard.update_scoreboard()

    # detect when turtle collides with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.goto(0, -300)
        scoreboard.level_up()
        car_manager.increase()
        car_manager.move_cars()

screen.exitonclick()
