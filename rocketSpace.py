# Click in the righthand window to make it active then use your arrow
# keys to control the spaceship!
import turtle

screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(600, 600)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("space0.gif")
# screen.bgcolor('black')

# Or, set the shape of a turtle
screen.addshape("rocketFi.gif")
turtle.shape("rocketFi.gif")

move_speed = 10
turn_speed = 10
turtle.right(90)
# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

pen = turtle.Turtle()
# Branding 
pen.penup()
pen.setpos(150,-270)
pen.pendown()
pen.pencolor('orange')
pen.write('Shubh Gurukul',font=("Arial", 18,"normal"))


turtle.mainloop()