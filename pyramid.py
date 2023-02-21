import turtle

def drawBlock():
    turtle.pendown()
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

def nextBlock():
    turtle.penup()
    turtle.forward(40)

def drawRow(length):
    for i in range(length):
        drawBlock()
        nextBlock()

def nextRow(back):
    turtle.penup()
    turtle.backward(back*40+20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

for i in range(10):
    drawRow(i+1)
    nextRow(i+1)
    
