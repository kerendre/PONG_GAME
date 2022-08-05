from turtle import Screen,write
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

GO_TO_COR_RIGTH = (350, 0)
GO_TO_COR_LEFT = (-350, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG PONG PONG PONG")

r_paddle = Paddle(GO_TO_COR_RIGTH)
l_paddle = Paddle(GO_TO_COR_LEFT)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

we_are_still_playing = True

while we_are_still_playing:
    ball.move_ball()

    # Checking if the ball is touched the top or bottom wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bouncing_y()

    # Checking if the ball touched the rigth paddle, if yes make the ball bounce
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 325:
        ball.bouncing_x()

    # Checking if the ball touched the rigth paddle, if yes make the ball bounce
    if ball.distance(l_paddle) <= 50 and ball.xcor() < -325:
        ball.bouncing_x()

    # Checking if the ball missed the left paddle, if yes add a point to the rigth player.
    # Showing updated scoreboard
    if ball.xcor() < -380:
        scoreboard.add_point_r()
        ball.restart_game()

    # Checking if the ball missed the rigth paddle, if yes add a point to the left player.
    # Showing updated scoreboard
    if ball.xcor() > 380:
        scoreboard.add_point_l()
        ball.restart_game()

screen.exitonclick()
