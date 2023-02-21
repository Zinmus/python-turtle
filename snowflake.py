import turtle

def bigSnow():
    turtle.pendown()
    turtle.forward(100)
    for i in range(8):
        smallSnow()
    turtle.penup()
    turtle.backward(100)
    turtle.right(45)

def smallSnow():
    turtle.pendown()
    turtle.forward(30)
    turtle.penup()
    turtle.backward(30)
    turtle.right(45)

for i in range(8):
    bigSnow()
