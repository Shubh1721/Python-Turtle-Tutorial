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
colors = [ "red","purple","blue","green","orange","yellow"]
for i in range(360):
    pen.pencolor(colors[i % 6])
    pen.forward(i+100)
    pen.width(i/100+1)
    pen.left(100)



# Branding 
pen.penup()
pen.setpos(150,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"normal"))

# Hide turtle
pen.hideturtle()
turtle.mainloop()