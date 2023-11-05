import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(253, 253, 249), (243, 234, 76), (211, 158, 93), (188, 12, 69), (111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166), (160, 78, 35), (128, 186, 146), (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95), (234, 165, 194), (79, 13, 63), (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
