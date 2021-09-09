#Video Link: https://www.youtube.com/watch?v=fg3sTVQp7nA

import random as rn
import turtle

win = turtle.Screen()
win.bgcolor('black')
win.title('Random Circle')

pen = turtle.Pen()
pen.speed(0)

# r, g, b must lie between 0 to 1
def random_circle(r, g, b):
    pen.color(r,g,b)
    pen.begin_fill()
    radius = rn.randint(10,100)
    pen.circle(radius)
    pen.end_fill()
    x = rn.randint(-500,500)
    y = rn.randint(-200,200)
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

for i in range(0,200):
    red = rn.randint(0,100)/100.0
    green = rn.randint(0,100)/100.0
    blue = rn.randint(0,100)/100.0
    random_circle(red, green, blue)

turtle.mainloop()   
