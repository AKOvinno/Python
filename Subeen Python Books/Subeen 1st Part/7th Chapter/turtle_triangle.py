import turtle

turtle.speed(2)

def draw_triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

draw_triangle(100)
turtle.exitonclick()
