from turtle import Turtle,Screen
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars= []
        self.speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.color(choice(COLORS))
        random_y = randint(-230,230)
        new_car.goto(300,random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_car_speed(self):
        self.speed =+ MOVE_INCREMENT
