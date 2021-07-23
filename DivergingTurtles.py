import turtle
pen = turtle.Turtle()

turtle.penup()
turtle.setpos(-100,250)
turtle.pendown()
turtle.pencolor('olive')
turtle.write('Fifty Shades of Grey',font=("Arial", 18,"bold"))
turtle.penup()
turtle.speed(0)
turtle.setpos(0,0)
turtle.pendown()
turtle.color("black","white")
turtle.colormode(1.0)
SQUARES = 50
SIDE = 150
shade = 1.0
for count in range(SQUARES):
    turtle.fillcolor(shade,shade,shade)
    turtle.begin_fill()   
    turtle.left(360//SQUARES)
    for side in  range(4):
        turtle.forward(SIDE)
        turtle.left(90)
        turtle.end_fill()
        shade -= turtle.colormode()/float(SQUARES)

# turtle.penup()
# turtle.setpos(150,-270)


turtle.done()
turtle.mainloop()

# import turtle
# # import random
# # import time

# screen=turtle.Screen()
# trtl=turtle.Turtle()
# screen.setup(420,320)
# screen.bgcolor('lightblue')
# trtl.shape('turtle')
# trtl.color('darkgoldenrod','black')
# s=10
# trtl.penup()
# trtl.setpos(30,30)
# for i in range(50):
#     s=s+2
#     trtl.stamp()
#     trtl.forward(s)
#     trtl.right(25)
#     # time.sleep(0.25) #activated with a break of a 1/4th of a second


# turtle.mainloop()
