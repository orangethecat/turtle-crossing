from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,265)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def write_game_over(self):
        self.clear()
        self.write_level()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))

    def write_winner(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WON!!!", align="center", font=("Courier", 50, "normal"))
