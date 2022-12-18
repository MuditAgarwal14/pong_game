import turtle
from turtle import Turtle

user_paddle = turtle.textinput("Chose color", "Chose the color of the PADDLE\nDon't chose black")


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        turtle.tracer(0)
        self.shape('square')
        self.color(user_paddle)
        self.penup()
        self.goto(coordinates)
        self.setheading(90)
        self.shapesize(stretch_len=5)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

