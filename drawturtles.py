__author__ = 'adam.mulroy'

import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.forward(100)

    window.exitonclick()


draw_square()