#Background will scroll when you press left or right arrow key

import turtle

wn = turtle.Screen()
wn.bgcolor('black')
wn.screensize(800, 360)
wn.tracer(100)
wn.title('Scrolling Background @ShubhGurukul')
wn.register_shape('Nature.gif')

player = turtle.Turtle()
player.color('deepskyblue')
player.shape('square')
player.shapesize(10, 20)
player.penup()
player.speed(0)

def left():
    global camera_dx
    camera_dx = 3
    # player.forward(camera_dx)

def right():
    global camera_dx
    camera_dx = -3
    # player.backward(camera_dx)
wn.listen()
wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')

camera_x = 0
camera_dx = 0

while True:
    camera_x += camera_dx
    camera_x %= 800

    player.goto(camera_x, 0)
    
    player.shape('Nature.gif')
    player.shapesize(10,20)
    player.stamp()


    player.goto(camera_x-800, 0)
    player.stamp()
    player.goto(camera_x+800, 0)
    player.stamp()


    wn.update()
    player.clear()

turtle.mainloop()
