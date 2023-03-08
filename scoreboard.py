from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 290)
        self.write(f"LEVEL: {self.level}", align="left", font=("Courier", 60, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game OVer", align="center", font=("Courier", 60, "normal"))

    def level_up(self):
        self.level += 1
        self.update_scoreboard()