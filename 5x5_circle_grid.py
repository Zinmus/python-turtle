import turtle
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()

def drawRow():
    for i in range(5):
        turtle.pendown()
        turtle.circle(30)
        turtle.penup()
        turtle.forward(60)

def nextRow():
    turtle.backward(300)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)

for i in range(5):
    drawRow()
    nextRow()
