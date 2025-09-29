import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#note that the winning level must
#be set to one higher than the actual winning level
WINNING_LEVEL = 4


screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSSING")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    random_chance = random.randint(0, 2)

    #creates a random chance to create a car
    if random_chance == 1:
        car_manager.create_cars()

    car_manager.move_cars()

    #detects when players at finish
    if player.ycor() == 280:
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_car_speed()

    #detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_is_on = False

    #detect when player won
    if scoreboard.level == WINNING_LEVEL:
        game_is_on = False


if scoreboard.level == WINNING_LEVEL:
    scoreboard.write_winner()
else:
    scoreboard.write_game_over()

screen.exitonclick()
