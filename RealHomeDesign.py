import turtle

# Screen Setup
screen = turtle.Screen()
screen.setup(1200,720)
screen.bgcolor("green")

# Pen Setup
pen = turtle.Turtle()
pen.shapesize(3,3,3)
pen.shape("turtle")
pen.speed(0)

# Ghar ka outer
pen.penup()
pen.goto(-400,0)
pen.pendown()

pen.color("red", "deepskyblue")
pen.begin_fill()
for i in range(2):
    pen.forward(800)
    pen.left(90)
    pen.forward(370)
    pen.left(90)
pen.end_fill()

# Home inner Part
pen.penup()
pen.goto(-100,0)
pen.pendown()

pen.color("red", "orange")
pen.begin_fill()
for i in range(2):
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
pen.end_fill()


# Ghar ki Chimeney
pen.penup()
pen.goto(50,200)
pen.pendown()

pen.color("red", "brown")
pen.begin_fill()
for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(130)
    pen.left(90)
pen.end_fill()


# Ghar Ki Topi
pen.penup()
pen.goto(-100,200)
pen.pendown()

pen.color("brown", "firebrick")
pen.begin_fill()

for i in range(3):
    pen.forward(200)
    pen.left(120)

pen.end_fill()

# Door of The ghar
pen.penup()
pen.goto(-25,0)
pen.pendown()

pen.color("brown", "red")
pen.begin_fill()

for i in range(2):
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)

pen.end_fill()

# Left Window 
pen.penup()
pen.goto(-70,120)
pen.pendown()
pen.pensize(3)
pen.color("black", "white")
pen.begin_fill()

for i in range(4):
    pen.forward(40)
    pen.left(90)

pen.end_fill()

# Vertical Line
pen.forward(20)
pen.left(90)
pen.forward(40)

# pen.stamp()


# Horizontal line
pen.penup()
pen.goto(-70, 140)
pen.pendown()
pen.right(90)
pen.forward(40)

# Right Window
pen.penup()
pen.goto(30,120)
pen.pendown()

pen.color("black", "white")
pen.begin_fill()

for i in range(4):
    pen.forward(40)
    pen.left(90)

pen.end_fill()


# Sun 

pen.penup()
pen.goto(-250, 250)
pen.pendown()

pen.color("red", "yellow")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Clouds

pen.penup()
pen.goto(250, 250)
pen.pendown()

pen.color("white", "white")
pen.begin_fill()
pen.circle(40)


pen.penup()
pen.goto(270, 230)
pen.pendown()

pen.circle(40)

pen.end_fill()



pen.hideturtle()
turtle.mainloop()