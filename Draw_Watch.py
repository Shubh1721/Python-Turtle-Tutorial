import turtle

# Screen Set up
screen = turtle.Screen()
screen.bgcolor("black")
screen.bgpic("sarswati.gif")

# Pen Set up
pen = turtle.Turtle()
pen.pensize(20)
pen.shape("turtle")
pen.shapesize(3,3,3)
pen.pencolor("blue")
pen.speed(0)
# 

pen.penup()
pen.goto(0,-300)
pen.pendown()
pen.circle(300)

# Inner Part of Watch

pen.pensize(10)
pen.pencolor("red")
pen.penup()
pen.home()
pen.left(90)
for i in range(12):
    pen.penup()
    pen.right(30)
    pen.goto(0,0)
    pen.forward(200)
    pen.pendown()
    pen.forward(25)

    pen.penup()
    pen.forward(30)
    pen.pendown()
    
    pen.write(str(i+1),align="center",font=("Arial", 18,"bold"))



# Branding 
pen.penup()
pen.setpos(180,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"bold"))

# Hide turtle
pen.hideturtle()
turtle.mainloop()