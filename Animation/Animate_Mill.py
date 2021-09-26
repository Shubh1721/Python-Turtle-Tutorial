# Simulation of Real Wind Mill with python turtle- How the fan moves and how it stops.

import turtle
# Making Window
wn = turtle.Screen()
wn.bgcolor('black')

mill = turtle.Turtle()
mill.pensize(5)
mill.color('red')
# mill.shapesize(4,4)
mill.left(75)
mill.speed(0)
# Taking coordinates of mill fan 
mill.begin_poly()
for i in range(3):
    mill.forward(100)
    mill.left(105)
    if i==0:
        x = mill.xcor()
    mill.forward(2*x)
    mill.left(105)
    mill.forward(100)
    mill.right(90)
mill.end_fill()

wn.register_shape('Mill', mill.get_poly())
wn.reset()
mill.shape('Mill')
mill.color('blue', 'red')
mill.turtlesize(outline =5)

mill.left(90)
mill.penup()
mill.backward(120)
mill.pendown()
mill.pencolor('purple')

mill.pensize(20)
mill.forward(220)
mill.pencolor('blue')
angle_vel = 3
for i in range(800):
    mill.left(angle_vel)
    angle_vel -= 0.009
   
turtle.mainloop()
