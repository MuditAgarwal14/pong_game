from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle.pos()) < 50 and ball.xcor() > 320\
            or ball.distance(l_paddle.pos()) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.8

    if ball.xcor() > 380:
        time.sleep(1)
        ball.goto(0, 0)
        ball.bounce_x()
        score.l_point()
        ball.move_speed = 0.1

    if ball.xcor() < -388:
        time.sleep(1)
        ball.goto(0, 0)
        ball.bounce_x()
        score.r_point()
        ball.move_speed = 0.1

screen.exitonclick()
