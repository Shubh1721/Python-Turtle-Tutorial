import turtle 
turtle.shapesize(3,3,3)
turtle.pensize(5)

turtle.speed(0)

def onDrag(x,y):
    
    turtle.ondrag(None) # don't do backtracking
    turtle.goto(x,y)

    turtle.ondrag(onDrag) # add new position

def mouseClick(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.listen()
turtle.ondrag(onDrag) # for dragging
turtle.onscreenclick(mouseClick) # for mouse click

turtle.mainloop()