import turtle

paper = turtle.Screen

pen = turtle.Turtle()

num_side = 4
side_length = 100

for _ in range(4):
    pen.forward(side_length)
    pen.left(90)

turtle.done()