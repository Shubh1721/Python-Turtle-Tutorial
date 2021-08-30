import turtle 
turtle.shapesize(3,3,3)
turtle.pensize(5)

turtle.speed(0)

def colorChangeR(): 
    turtle.pencolor('red')

def colorChangeB():
    turtle.pencolor('blue')

def colorChangeG():
    turtle.pencolor('green')

def colorChangeP():
    turtle.pencolor('purple')

def eraser():
    # turtle.pensize(50)
    turtle.pencolor('white')
global size
size = 5
def incrPenSize():
    global size
    turtle.pensize(size)
    size = size+5

def dcrPenSize():
    global size
    turtle.pensize(size)
    if size>5:
        size = size-5

def onDrag(x,y):
    
    turtle.ondrag(None) # don't do backtracking
    turtle.goto(x,y)

    turtle.ondrag(onDrag) # add new position

def mouseClick(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.listen()

turtle.onkey(colorChangeR,'r')
turtle.onkey(colorChangeB,'b')
turtle.onkey(colorChangeG,'g')
turtle.onkey(colorChangeP,'p')
turtle.onkey(eraser, '0')
turtle.onkey(incrPenSize, 'Up')
turtle.onkey(dcrPenSize, 'Down')

turtle.ondrag(onDrag) # for dragging
turtle.onscreenclick(mouseClick) # for mouse click

turtle.mainloop()























# import turtle 
# turtle.shapesize(3,3,3)
# turtle.pensize(5)
# turtle.bgcolor('black')
# turtle.pencolor('white')
# turtle.speed(0)
# def changeColorR():
#     turtle.pencolor('red')
# def changeColorG():
#     turtle.pencolor('green')
# def changeColorB():
#     turtle.pencolor('blue')
# def changeDefault():
#     turtle.pencolor('white')        
# def onDrag(x,y):
    
#     turtle.ondrag(None) # don't do backtracking
#     turtle.goto(x,y)

#     turtle.ondrag(onDrag) # add new position

# def mouseClick(x,y):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
# key='R'

# turtle.listen()
# turtle.onkey(changeDefault, '0')
# turtle.onkey(changeColorR,'r')
# turtle.onkey(changeColorB,'b')
# turtle.onkey(changeColorG,'g')

# turtle.ondrag(onDrag) # for dragging
# turtle.onscreenclick(mouseClick) # for mouse click


# turtle.mainloop()

# # def changeColor():
# #     # if key=='R':
# #     turtle.pencolor('red')
#     # if key == 'O':
#     #     turtle.color('Orange')
#     # if key == 'B':
#     #     turtle.color('Black')
#     # if key == 'U':
#     #     turtle.color('Blue')
#     # if key == 'P':
#     #     turtle.color('Pink')
        
