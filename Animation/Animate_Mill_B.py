# Mill Fan freely moving away from the pole.
#Simulate the mill fan according to physics how a fan looks when this will free from the pole.

import turtle
wn = turtle.Screen()
wn.bgcolor('black')

mill = turtle.Turtle()
mill.pensize(5)
mill.color('red')
# mill.shapesize(4,4)
mill.left(75)
mill.speed(0)

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
mill.turtlesize(3)

angle_vel = 3
for i in range(360):
    mill.left(angle_vel)    

angle_vel = 2
# x=0
# y=100
mill.penup()
factor = 3
mill.turtlesize(factor)
vel =1
for i in range(200):
    angle_vel += .4
    mill.left(angle_vel)
    if i>70:
        factor *=0.985
        vel *= 1.01
        x,y = mill.pos()
        mill.setpos(x+vel, y+vel)
        mill.turtlesize(factor)




turtle.mainloop()
