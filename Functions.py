import turtle

# Screen Set up
screen = turtle.Screen()
screen.bgcolor("black")

# Pen Set up
pen = turtle.Turtle()
pen.pensize(5)
pen.shape("turtle")
pen.shapesize(3,3,3)
pen.pencolor("red")

pen.speed(0)
# 
def drawCircle(rad, color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()

drawCircle(100,"yellow")

pen.penup()
pen.goto(-40,120)
pen.pendown()

drawCircle(20,"white")

pen.penup()
pen.goto(40,120)
pen.pendown()

drawCircle(20,"white")

pen.penup()
pen.goto(0,50)
pen.pendown()

drawCircle(20,"white")



# Branding 
pen.penup()
pen.setpos(150,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"normal"))

# Hide turtle
pen.hideturtle()
turtle.mainloop()
