from turtle import Turtle

MOVE_DISTANCE = 30
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, go_to_cor):
        super().__init__()
        self.penup()
        self.goto(go_to_cor)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.speed("fastest")

    def move_paddle(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        if self.heading() != UP:
            self.shapesize(1, 5)
            self.setheading(UP)
        else:
            self.move_paddle()

    def down(self):
        if self.heading() != DOWN:
            self.shapesize(1, 5)
            self.setheading(DOWN)

        else:
            self.move_paddle()












