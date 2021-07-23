import turtle
pen = turtle.Turtle()


def drawCircle(rad, color):
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    pen.penup()

# draw face
drawCircle(100, "yellow")

pen.speed(0)
# draw eyes
pen.goto(-40, 120)
drawCircle(15, 'white')
pen.goto(-37, 125)
drawCircle(5, "black")
pen.goto(40, 120)
drawCircle(15, 'white')
pen.goto(40, 125)
drawCircle(5, "black")


# draw nose
pen.goto(0, 75)
drawCircle(8,"black")

# draw mouth
pen.goto(-40, 85)
pen.down()
pen.right(90)
pen.circle(40, 180)
pen.up()

# draw tongue
pen.goto(-10, 45)
pen.down()
pen.right(180)
pen.fillcolor('red')
pen.begin_fill()
pen.circle(10, 180)
pen.end_fill()
pen.hideturtle()

turtle.mainloop()