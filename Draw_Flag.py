import turtle as pen

pen.shapesize(3,3,3)
pen.pensize(1)
pen.colormode(255)
pen.speed(1)

def rectangle(x,y,color):
    pen.color(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(x)
        pen.left(90)
        pen.forward(y)
        pen.left(90)
    pen.end_fill()    

# Saffron Rectangle
pen.penup()
pen.goto(-300,100)
pen.pendown()
rectangle(800,180,(255,60,20)) # saffron color rgb value

# Green Rectangle
pen.goto(-300,-260)
rectangle(800,180,(0,255,0))

# Big Circle-Wheel
pen.penup()
pen.goto(100,-80)
pen.pendown()
pen.pensize(7)
pen.color(0,0,255)
pen.circle(90)

# Make stick
pen.penup()
pen.goto(100,10)
pen.pendown()
pen.dot(25)
pen.pensize(4)
for i in range(24):
    pen.forward(90)
    pen.backward(90)
    pen.left(15)

pen.penup()
pen.goto(-600,200)
pen.write("Tiranga",font=("Times",40))


pen.hideturtle()
pen.mainloop()