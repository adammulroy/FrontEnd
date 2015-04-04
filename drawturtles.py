__author__ = 'adam.mulroy'

import turtle


def draw_square(brad):
    n = 0
    while n < 4:
        brad.forward(120)
        brad.right(90)
        n += 1


def draw_circle(angie):
    angie.shape('arrow')
    angie.color('yellow')
    angie.circle(100)


def draw_triangle(triangle):
    triangle.shape('turtle')
    n = 1
    while n < 4:
        triangle.forward(120)
        triangle.right(120)
        n += 1


def draw_screen():
    window = turtle.Screen()
    window.bgcolor("red")

    square = turtle.Turtle()
    square.speed(5)
    for i in range(1, 73):
        draw_square(square)
        square.right(5)

    #draw_circle()
    #circle = turtle.Turtle()
    #draw_triangle(triangle)
    #triangle = turtle.Turtle()

draw_screen()