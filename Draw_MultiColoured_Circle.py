import turtle

# Screen Set up
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(620,620)
# Pen Set up

pen = turtle.Turtle()
pen.pensize(5)
pen.shape("turtle")
pen.shapesize(3,3,3)
pen.pencolor("red")

trtl=turtle.Turtle()
trtl.pensize(3)
trtl.speed(0)

n=-1
colors=['red','green','blue','yellow','purple']
for angle in range(0,360,20):
    n=n+1
    if n==5:
        n=-1
    trtl.color(colors[n])
    trtl.seth(angle)
    trtl.circle(100)





# Branding 
pen.penup()
pen.setpos(150,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"normal"))

# Hide turtle
pen.hideturtle()
turtle.mainloop()