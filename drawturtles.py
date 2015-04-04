__author__ = 'adam.mulroy'

import turtle

window = turtle.Screen()
window.bgcolor("red")


def draw_square():
    brad = turtle.Turtle()
    n = 0
    while n < 4:
        brad.forward(120)
        brad.right(90)
        n += 1


def draw_circle():
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('yellow')
    angie.circle(100)


def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape('turtle')
    n = 1
    while n < 4:
        triangle.forward(120)
        triangle.right(120)
        n += 1

draw_square()
draw_circle()
draw_triangle()
