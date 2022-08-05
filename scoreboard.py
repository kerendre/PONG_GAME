from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 22, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.score_l=0
        self.score_r = 0
        self.show_score()

    def add_point_r(self):
        self.score_r += 1
        self.show_score()

    def add_point_l(self):
        self.score_l += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.score_l}  :  {self.score_r}", move=False, align=ALIGN, font=FONT)
