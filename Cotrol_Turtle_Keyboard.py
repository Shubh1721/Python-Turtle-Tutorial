import turtle

turtle.Screen()
turtle.setup(500,500)
turtle.pensize(5)
turtle.shapesize(3,3,3)
turtle.shape("turtle")
turtle.color("red")
turtle.bgcolor("deepskyblue")
# pen.speed(0)

def forward():
    turtle.forward(10)

def backward():
    turtle.backward(10)

def left():
    turtle.left(10)

def right():
    turtle.right(10)

def fow(x,y):
    turtle.goto(x,y)
# turtle.listen()
# turtle.onclick(fow)    
turtle.listen()
turtle.ondrag(fow)
turtle.onkey(forward, "Up")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onkey(backward,"Down")

turtle.mainloop()