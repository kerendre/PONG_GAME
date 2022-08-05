from turtle import Turtle
import time


ball_on_court = True

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("pink")
        self.shape("circle")

        self.y_move = 5
        self.x_move = 5

    def move_ball(self):
        time.sleep(0.03)
        y_new = self.ycor()+self.y_move
        x_new = self.xcor()+self.x_move
        self.goto(x_new, y_new)

    def bouncing_y(self):
        self.y_move *= -1

    def bouncing_x(self):
        self.x_move *= -1

    def restart_game(self):
        self.goto(x=0, y=0)
        self.x_move *= -1
        self.move_ball






















        # detect collision with  top and bottom walls










    # def move_ball(self):
    #     while ball_on_court:
    #         self.setheading(ball_angle)
    #         self.fd(20)
    #         self.touch_top_bottom()
    #
    #
    # # detect collision with  top and bottom walls
    # def touch_top_bottom(self):
    #     if self.ycor()> 280 or self.ycor()<-280:













