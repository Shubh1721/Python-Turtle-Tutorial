import turtle

# Screen Set up
screen = turtle.Screen()
screen.bgcolor("black")

# Pen Set up
pen = turtle.Pen()
pen.pensize(5)
pen.shape("turtle")
pen.shapesize(3,3,3)
pen.pencolor("red")
pen.speed(0)

# 

colors = ["red", "blue", "green", "yellow", "purple"]
for j in range(100):
    for i in range(5):
        pen.circle(100)
        pen.left(20)
        pen.pencolor(colors[i])





# Branding 
pen.penup()
pen.setpos(150,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"normal"))

# Hide turtle
pen.hideturtle()
turtle.mainloop()
