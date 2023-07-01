import turtle

turtle.speed(2)

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

draw_square(100)
turtle.exitonclick()